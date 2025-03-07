L_name = []
L_contactnumber = []
L_email = []
L_city = []
L_state = []
L_gender = []
L_address = []
L_days = []
L_room_type = []
L_room_no = []
L_check_in_date = []
L_check_out_date = []
L_payment_type = []
Registration_info = {}
checkin_info = {}


print("-------Welcome to hotel management system----------")
print("""
               MENU:
    press 1 for registration
    press 2 for check in 
    press 3 for show guest list
    press 4 for check out
    press 5 for get info of any guest
    press 6 for exit
         """)
while True:
    choice = int(input("Enter your choice(1,2,3,4,5,6):"))
    if choice == 1:
        class Registration:
                def customer(self, name, contactNo, city, Gender, State, Email):
                        self.name = name
                        self.contactNo = contactNo
                        self.city = city
                        self.Gender = Gender
                        self.State = State
                        self.Email = Email
                        print("Registration Successfully Done As Customer")

                def get_data(self):
                    self.name = input("Enter Your Name:")

                    try:
                        self.contactNo = input("Enter Your Contact No:")
                        if not self.contactNo.isdigit():
                            raise ValueError("Contact number must contain only digits.")
                        if len(self.contactNo) != 10:
                            raise ValueError("Contact number must be exactly 10 digits long.")
                        print("Valid contact number entered.")
                    except ValueError as e:
                        print(f"Error: {e}")
                          
                    self.city = input("Enter Your City:")
                    self.Email = input("Enter Email id: ")
                    self.Gender = input("Enter Your Gender:")
                    self.state = input("Enter Your State:")

                def list_data(self):
                        L_name.append(self.name)
                        print(self.name)
                        L_contactnumber.append(self.contactNo)
                        print(self.contactNo)
                        L_email.append(self.Email)
                        print(self.Email)
                        L_city.append(self.city)
                        print(self.city)
                        L_state.append(self.state)
                        print(self.state)
                        L_gender.append(self.Gender)
                        print(self.Gender)

                def print_data(self):
                        print("Name:", self.name)
                        print("Contact No:", self.contactNo)
                        print("City:", self.city)
                        print("Email:", self.Email)
                        print("Gender:", self.Gender)
                        print("State:", self.state)

                def save_registration(self):
                        Registration_info[self.name] = {"Email": self.Email, "Gender": self.Gender, "city": self.city, "State": self.state, "Contact_no": self.contactNo}
                        print(Registration_info)

                        file = open('Registration.txt', 'a')
                        file.write(str(Registration_info) + "\n")
                        file.close()
                        print("Registration Successfully Done As Customer")

        reg = Registration()
        reg.get_data()
        reg.list_data()
        reg.print_data()
        reg.save_registration()

    elif choice == 2:
        class checkin(Registration):
             def check_in_data(self, name, contactNo, address, days, room_type, room_no, check_in_date, check_out_date,payment_type):
                        self.name = name
                        self.contactNo = contactNo
                        self.address = address
                        self.days = days
                        self.room_type = room_type
                        self.room_no = room_no
                        self.check_in_date = check_in_date
                        self.check_out_date = check_out_date
                        self.payment_type = payment_type
                        print("Check In Successfully Done")

             def guest_data(self):
                    self.name = input("Enter Your Name:")
                        
                    try:
                        self.contactNo = input("Enter Your Contact No:")
                        if not self.contactNo.isdigit():
                            raise ValueError("Contact number contain only digits.")
                        if len(self.contactNo) != 10:
                            raise ValueError("Contact number must be 10 digit ")
                        print("Valid contact number entered.")
                    except ValueError as e:
                        print(f"Error: {e}")
                        
                    self.address = input("Enter Your Address:")
                    self.days = int(input("Enter No of Days u want to stay:"))
                    self.room_type = input("""Enter Room Type 
                                           Delux for D:
                                           General for G:
                                            Full Delux Fd:
                                           Joint for j:""")
                    self.room_no = int(input("Enter Room No:"))
                    self.check_in_date = input("Enter Check In Date:")
                    self.check_out_date = input("Enter Check Out Date:")
                    self.payment_type = input("""Enter Payment Type:
                                                Cash for C:
                                                Card for Cr:""")
             def guest_list(self):
                   print("Guest List:")
                   L_name.append(self.name)
                   print(self.name)
                   L_contactnumber.append(self.contactNo)
                   print(self.contactNo)
                   L_address.append(self.address)
                   print(self.address)
                   L_days.append(self.days)
                   print(self.days)
                   L_room_type.append(self.room_type)
                   print(self.room_type)
                   L_room_no.append(self.room_no)
                   print(self.room_no)
                   L_check_in_date.append(self.check_in_date)
                   print(self.check_in_date)   
                   L_check_out_date.append(self.check_out_date)
                   print(self.check_out_date)  
                   L_payment_type.append(self.payment_type)
                   print(self.payment_type)

                    
             def guest_print_data(self):
                    print("Name:", self.name)
                    print("Contact No:", self.contactNo)
                    print("Address:", self.address)
                    print("Days:", self.days)
                    print("Room Type:", self.room_type)
                    print("Room No:", self.room_no)
                    print("Check In Date:", self.check_in_date)
                    print("Check Out Date:", self.check_out_date)
                    print("Payment Type:", self.payment_type)  
                    
             def save_guest_registration(self):
                    checkin_info[self.name] = {"Contact_no": self.contactNo, "Address": self.address, "Days": self.days, "Room_type": self.room_type, "Room_no": self.room_no, "Check_in_date": self.check_in_date, "Check_out_date": self.check_out_date, "Payment_type": self.payment_type}
                    print(checkin_info)
                    print("Checkin Successfully Done") 
                    file = open('checkin.txt', 'a')
                    file.write(str(checkin_info) + "\n")
                    file.close()
                    print("Checkin Successfully Done As Customer")  

        ck = checkin()
        ck.guest_data()
        ck.guest_list()
        ck.guest_print_data()
        ck.save_guest_registration()
    
    elif choice == 3:
        print("Guest List:")
        for name, info in Registration_info.items():
            print(f"Name: {name}, Info: {info}")
    
    elif choice == 4:
        class checkout(checkin):
            def check_out_data(self):
                self.name = input("Enter Your Name:")
                self.contactNo = input("Enter Your Contact No:")
                self.room_no = int(input("Enter Room No:"))
                self.check_out_date = input("Enter Check Out Date:")
                
                if self.name in checkin_info:
                    print(f"Checking out {self.name}")
                    del checkin_info[self.name] 
                    print(f"{self.name} has checked out successfully.")
                    with open('checkin.txt', 'w') as file:
                        for guest, details in checkin_info.items():
                            file.write(f"{guest}: {details}\n") 
                else:
                    print("Guest not found in check-in records.")

        co = checkout()
        co.check_out_data()

    elif choice == 5:
        guest_name = input("Enter the name of the guest to get info:")
        if guest_name in Registration_info:
            print(f"Guest Info: {Registration_info[guest_name]}")
        else:
            print("Guest not found.")

    elif choice == 6:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice")

                        
               
                
