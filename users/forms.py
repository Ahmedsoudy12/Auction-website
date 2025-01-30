from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Gender"
    )
    notify_me = forms.BooleanField(
        required=False,
        label="Notify me via email with the news!"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'notify_me']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }