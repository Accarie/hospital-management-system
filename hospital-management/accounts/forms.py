from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from hospital.models import AdminProfile

class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    position = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'position']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            AdminProfile.objects.create(user=user, position=self.cleaned_data['position'])
        return user

class AdminLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
