from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.id}: {self.email}'