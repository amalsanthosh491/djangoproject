from django.db import models

# Create your models here.
class Register(models.Model):
   Name=models.CharField(max_length=10)
   Age=models.IntegerField()
   Place=models.CharField(max_length=20)
   Email=models.EmailField()
   Password=models.CharField(max_length=8)

class Image(models.Model):
   Name=models.CharField(max_length=10)
   Age=models.IntegerField()
   Place=models.CharField(max_length=20)
   Photo=models.ImageField(upload_to='media/',null=True,blank=True)
   Email=models.EmailField()
   Password=models.CharField(max_length=8)