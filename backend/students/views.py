from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all().order_by('-joined_at')
    serializer_class=StudentSerializers
