from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re

# Create your models here.

def validate_phonenumber(value):
    pattern = re.compile("^[0-9 -]{9,30}$")
    if not pattern.match(value):
        raise ValidationError("Invalid Phone number")

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,null=False, unique=True)
    phone = models.CharField(max_length=50,validators=[validate_phonenumber])
    isAdmin = models.BooleanField(default=False)

    def isAdminUser(self):
        return self.isAdmin



