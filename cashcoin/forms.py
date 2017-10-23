from django.forms import PasswordInput, ModelForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]
        help_texts = {
            'username': None,
        }
        widgets = {
            'password': PasswordInput(),
        }

