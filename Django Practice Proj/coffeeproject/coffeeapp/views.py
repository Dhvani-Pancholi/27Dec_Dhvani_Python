from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from .forms import *
from .models import *

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(email, otp):
    subject = 'Your OTP for Coffee Shop Registration'
    message = f'Your OTP for registration is: {otp}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def register(request):
    if request.method == 'POST':
        if 'otp' in request.POST:
            otp_form = OTPVerificationForm(request.POST)
            if otp_form.is_valid():
                stored_otp = request.session.get('otp')
                if stored_otp == otp_form.cleaned_data['otp']:
                    # Create user and profile
                    form_data = request.session.get('form_data')
                    form = UserRegistrationForm(form_data)
                    if form.is_valid():
                        user = form.save()
                        login(request, user)
                        messages.success(request, 'Registration successful! Welcome to Coffee Shop.')
                        return redirect('home')
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
        else:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                # Store form data in session
                request.session['form_data'] = request.POST
                # Generate and send OTP
                otp = generate_otp()
                request.session['otp'] = otp
                send_otp_email(form.cleaned_data['email'], otp)
                messages.info(request, 'OTP has been sent to your email.')
                return render(request, 'coffeeapp/register.html', {'otp_sent': True, 'otp_form': OTPVerificationForm()})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'coffeeapp/register.html', {'form': form, 'otp_sent': False})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'coffeeapp/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'coffeeapp/profile.html', {'form': form})

def home(request):
    coffee_items = CoffeeItem.objects.filter(is_available=True)
    return render(request, 'coffeeapp/home.html', {'coffee_items': coffee_items})

@login_required
def menu(request):
    coffee_items = CoffeeItem.objects.filter(is_available=True)
    return render(request, 'coffeeapp/menu.html', {'coffee_items': coffee_items})

@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.coffee_item.price * item.quantity for item in cart_items)
    return render(request, 'coffeeapp/cart.html', {'cart_items': cart_items, 'total': total})


    
@login_required
def add_to_cart(request, item_id):
    coffee_item = CoffeeItem.objects.get(id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, coffee_item=coffee_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f'{coffee_item.name} added to cart!')
    return redirect('menu')

@login_required
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    messages.info(request, 'Item removed from cart.')
    return redirect('cart')

@login_required
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
    if not cart_items.exists():
        messages.error(request, 'Your cart is empty!')
        return redirect('cart')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_amount = sum(item.coffee_item.price * item.quantity for item in cart_items)
            order.save()
            
            # Create order items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    coffee_item=cart_item.coffee_item,
                    quantity=cart_item.quantity,
                    price=cart_item.coffee_item.price
                )
            
            # Clear cart
            cart_items.delete()
            
            # Send confirmation email
            subject = 'Order Confirmation - Coffee Shop'
            message = f'Thank you for your order! Your order number is #{order.id}.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [request.user.email]
            send_mail(subject, message, from_email, recipient_list)
            
            messages.success(request, 'Order placed successfully!')
            return redirect('orders')
    else:
        form = OrderForm()
    
    return render(request, 'coffeeapp/place_order.html', {'form': form, 'cart_items': cart_items})

@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'coffeeapp/orders.html', {'orders': orders})
