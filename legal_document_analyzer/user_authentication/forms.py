from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User


class HostSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(HostSignUpForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field_name.capitalize()}'
            })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {self.fields[field_name].label}'
            })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
        


class SetPasswordCustomForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(SetPasswordCustomForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {self.fields[field_name].label}'
            })