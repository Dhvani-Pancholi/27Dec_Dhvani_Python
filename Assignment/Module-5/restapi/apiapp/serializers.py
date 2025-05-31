from rest_framework import serializers
from .models import *


class DrSerial(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"