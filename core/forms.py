from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

## formulario de registro personalziado

class CustomedUserCreationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    email = forms.EmailField(label='Correo Electrónico', required=True)  

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(username=email).exists():
            raise ValidationError("Ya existe un usuario registrado con este correo electrónico.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  
        user.username = self.cleaned_data['email']  ## el correo como nombre de usuario

        if commit:
            user.save()
        return user
