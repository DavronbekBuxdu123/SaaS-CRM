from django.db import models
from courses.models import Group
# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=255,verbose_name="Ismi")
    last_name=models.CharField(max_length=255,verbose_name="Familiyasi")
    phone=models.CharField(max_length=100,verbose_name='Telefon')
    groups=models.ManyToManyField(Group,verbose_name='Guruhi',related_name='students')
    joined_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

