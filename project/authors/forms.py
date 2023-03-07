from django import forms
from django.contrib.auth.models import User
# Meus formulários:

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        })
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        })
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-container'
        })
    )

