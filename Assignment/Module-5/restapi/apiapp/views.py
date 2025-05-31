from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

#getdata
@api_view(["GET"])
def getalldata(request):
    drdata = Doctor.objects.all()
    serial = DrSerial(drdata, many=True)
    return Response(serial.data)

#getid
@api_view(["GET"])
def getdrid(request, id):
    try:
        drid = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = DrSerial(drid)
    return Response(data=serial.data)

#insert
@api_view(["POST"])
def savedata(request):
    if request.method == "POST":
        serial = DrSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
#delete and get
@api_view(["DELETE", "GET"])
def deletedrid(request, id):
    try:
        drid = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serial = DrSerial(drid)
        return Response(data=serial.data)
    if request.method == "DELETE":
        Doctor.delete(drid)
        return Response(status=status.HTTP_202_ACCEPTED)
    
# update and get
@api_view(["PUT", "GET"])
def updatedata(request, id):
    try:
        drid = Doctor.objects.get(id=id)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serial = DrSerial(drid)
        return Response(data=serial.data)
    if request.method == "PUT":
        serial = DrSerial(data=request.data, instance=drid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
