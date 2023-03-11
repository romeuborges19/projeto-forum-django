from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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

    error_css_class = 'error'

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container',
        }),
        label='Seu primeiro nome'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        }),
        label='Seu último nome'
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        }),
        label='Seu nome de usuário',
        max_length=20,
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-container'
        }),
        label='Seu e-mail'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-container'
        }),
        label='Insira sua senha'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-container',
        }),
        label='Confirme sua senha'
    )


    error_messages = {
        'username':{
            'required':'Este campo é obrigatório',
            'already_exists':'Esse nome de usuário já existe',
            'max_length':'O nome de usuário deve ter menos de 20 caracteres.'
        },
        'first_name':{
            'required':'Este campo é obrigatório',
        },
        'last_name':{
            'required':'Este campo é obrigatório',
        },
        'email':{
            'required':'Este campo é obrigatório',
        },
        'password':{
            'required':'Este campo é obrigatório'
        }
    }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        exists = User.objects.filter(username=username).exists()

        if exists:
            raise ValidationError(
                'Nome de usuárío já está em uso'
            )
        return username

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError(
                'As senhas devem ser iguais'
            )

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email', '')

        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'E-mail já está em uso.',
                code = 'invalid'
            )

        return email
