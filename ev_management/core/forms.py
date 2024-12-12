from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import your custom User model

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Use your custom User model
        fields = ['username', 'email', 'password1', 'password2']



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['center', 'slot']  # Adjusted the fields as per your model definition
