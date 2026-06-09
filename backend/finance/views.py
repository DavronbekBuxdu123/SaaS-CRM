from django.shortcuts import render
from .models import Payment
from rest_framework import viewsets
from .serializers import PaymentSerializers
# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all().order_by('-paid_at')
    serializer_class=PaymentSerializers