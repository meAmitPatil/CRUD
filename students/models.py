from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return f"{self.f_name} {self.l_name}"
