from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def getalldata(request):
    tsdata = Task.objects.all()
    serial = taskSerial(tsdata, many=True)
    return Response(data=serial.data)

@api_view(["GET"])
def gettid(request, id):
    try:
        tid = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = taskSerial(tid)
    return Response(data=serial.data)


@api_view(["DELETE", "GET"])
def deletetid(request, id):
    try:
        tid = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serial = taskSerial(tid)
        return Response(data=serial.data)
    if request.method == "DELETE":
        Task.delete(tid)
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(["POST"])
def savedata(request):
    if request.method == "POST":
        serial = taskSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "GET"])
def updatedata(request, id):
    try:
        tid = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serial = taskSerial(tid)
        return Response(data=serial.data)
    if request.method == "PUT":
        serial = taskSerial(data=request.data, instance=tid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)