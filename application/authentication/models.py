from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_sales_manager = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)


class Staff(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="user_staff")
    last_name = models.CharField(max_length=255, name="Last Name")
    first_name = models.CharField(max_length=255, name="First Name")
    address = models.CharField(max_length=255, name="Address")
    contact = models.CharField(max_length=255, name="Contact Number")
