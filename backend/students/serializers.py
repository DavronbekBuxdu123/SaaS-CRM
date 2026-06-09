from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        fields="__all__"