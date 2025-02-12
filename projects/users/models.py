from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(("email address"), unique=True)
    phone_number = models.CharField(max_length=11)
    USERNAME_FIELD = "email"
    is_staff = models.BooleanField(default=True)
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "phone_number",
        
    ]
    def __str__(self):
        return "{}".format(self.email)
