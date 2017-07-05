"""
from django.contrib.auth.models import User
get_user_model method will return the currently active user model, settings.AUTH_USER_MODEL default auth.user
"""
 from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'
