from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Create
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
        
# Update        
class CustomUserUpdateForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
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
        fields = ['username', 'email', 'gender', 'notify_me', 'profile_picture']  # Fields the user can update

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})  