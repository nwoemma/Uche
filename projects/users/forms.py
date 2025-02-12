from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import authenticate

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=11)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    class Meta:
        model = User
        fields = ["email", "username", "phone_number"]

class UserLoginForm(forms.ModelForm):
    username = forms.EmailField(label="Email")

    def clean(self):
        email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("Invalid login credentials.")
        return self.cleaned_data

class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]