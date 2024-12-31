from django import forms
from django.contrib.auth.models import User
from .models import registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = ['full_name', 'phone', 'pet_info', 'address','roll']  # Fields from the registration model
