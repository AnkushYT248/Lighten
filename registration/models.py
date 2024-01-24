from django.db import models

class CustomModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.FileField(upload_to='check/',max_length=250,null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#class Cloth(models.Model):
   # name = models.CharField(max_length=100)
   # description = models.TextField()
   # price = models.DecimalField(max_digits=5, decimal_places=2)
    #image = models.ImageField(upload_to='cloths/')