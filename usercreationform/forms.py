from django import forms
from .models import authent
from django.contrib.auth.forms import UserCreationForm


class authenticateform(UserCreationForm):
    class Meta:
        Model : authent
        fields = '__all__'
