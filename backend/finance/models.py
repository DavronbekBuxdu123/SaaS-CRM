from django.db import models
from students.models import Student
# Create your models here.

class Payment(models.Model):
    PAYMENT_TYPE_CHOICES=[
        ('cash',"Naqd"),
        ('card',"Karta"),
        ("online","Humo / Payme / Apelsin")]
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='payments',verbose_name="O'quvchi")
    amount=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="To'lov summasi")
    payment_type=models.CharField(max_length=20,choices=PAYMENT_TYPE_CHOICES,default='cash',verbose_name="To'lov usuli")
    paid_at=models.DateTimeField(auto_now_add=True,verbose_name="To'langan vaqti")
  
    def __str__(self):
        return f"{self.student.first_name}-{self.amount}"