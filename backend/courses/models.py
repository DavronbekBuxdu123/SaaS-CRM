from django.db import models

# Create your models here.

class Course(models.Model):
    title=models.CharField(max_length=255,verbose_name='Kurs nomi')
    description=models.TextField(verbose_name='Kurs haqida...',blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Kurs narxi')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Group(models.Model):
    DAYS_CHOICES = [
    ('odd', 'Toq kunlar (Du-Chor-Ju)'),
    ('even', 'Juft kunlar (Se-Pay-Sha)'),
    ('everyday', 'Har kuni'),
    ('weekend', 'Dam olish kunlari (Sha-Yak)'),
]
    title=models.CharField(max_length=100,verbose_name='Guruh nomi')
    teacher_name=models.CharField(verbose_name="Guruh o'qituvchisi",max_length=255)
    lesson_started=models.TimeField(verbose_name="Dars boshlanish vaqti")
    days=models.CharField(max_length=20,choices=DAYS_CHOICES,default='odd',verbose_name='Dars kunlari')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='groups')

    def __str__(self):
        return f"{self.title}-{self.course.title}"
