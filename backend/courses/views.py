from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all().order_by('-created_at')
    serializer_class=CourseSerializer