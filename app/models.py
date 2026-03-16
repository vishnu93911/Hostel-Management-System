from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

password_validator = RegexValidator(
    regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,16}$',
    message="Password must contain 1 uppercase, 1 lowercase, 1 number, 1 special character and be 8-16 characters long."
)
phonenumber_validator = RegexValidator(
    regex=r'^[6-9][0-9]{9}$',
    message="Phone number must start with 6,7,8,9 and contain exactly 10 digits."
)

class RegisteredUsers(models.Model):
    username = models.CharField(max_length=64, unique=True)
    phone_number=models.CharField(unique=True,
        max_length=255,  
        validators=[phonenumber_validator]
    )
    email=models.EmailField(unique=True)
    age=models.IntegerField(default=0)
    address = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(
        max_length=255,
        validators=[password_validator]
    )
    
    def __str__(self): 
        return self.username
    


    