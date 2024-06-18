from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    birth_date=models.DateField(max_length=20)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    hire_date=models.DateField(max_length=20)
    def __str__(self):
        return self.first_name+self.last_name