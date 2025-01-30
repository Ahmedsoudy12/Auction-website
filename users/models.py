from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields if needed
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    notify_me = models.BooleanField(default=False)  # Checkbox for email notifications

    def __str__(self):
        return self.username