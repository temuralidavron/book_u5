from django import forms
from .models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'phone','password']

    def save(self, commit=True, *args, **kwargs):
        return CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            last_name=self.cleaned_data['last_name'])


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
