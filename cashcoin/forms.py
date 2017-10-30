#!/Users/escobar/anaconda/bin/python
from django import forms
from django.forms import PasswordInput, TextInput, ModelForm, Form
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]
        help_texts = {
            'username': None,
        }
        widgets = {
            'username': TextInput(attrs={'class':'form-control',
                                         'placeholder':'User Name',}
                                 ),
            'password': PasswordInput(attrs={'class':'form-control',
                                             'placeholder':'Password',}
                                     ),
        }

class SignupForm(UserForm):
    repeat_password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control',
                                                                  'placeholder':'Repeat Password',
                                                                 }))
    class Meta(UserForm.Meta):
        fields = UserForm.Meta.fields + ['repeat_password']
