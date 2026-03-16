from django.db import models

# Create your models here.

class Hostel(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rooms = models.IntegerField()
    tenants = models.IntegerField(default=0)
    rent = models.IntegerField()

    def __str__(self):
        return self.name
    
class Tenant(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.IntegerField()

    def __str__(self):
        return self.name