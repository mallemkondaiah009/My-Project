from django.db import models
from django.contrib.auth.models import User  # Use Django's default User model

# models.py in your 'core' app
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Add custom fields if needed
    pass


class EVCenter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use the default User model
    center = models.ForeignKey(EVCenter, on_delete=models.CASCADE)
    slot = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.center.name} - {self.slot}"

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    )
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
