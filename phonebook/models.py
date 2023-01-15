from django.contrib.auth.models import User
from django.db import models


class ContactInfo(models.Model):
    phone_choices = (
        ('M', 'Mobile'),
        ('W', 'Work'),
        ('H', 'Home'),
        ('O', 'Office')
    )
    contact_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=11, unique=True, null=False)
    phone_type = models.CharField(max_length=10, choices=phone_choices, default='M')
    user = models.ForeignKey(User, on_delete=models.CASCADE)