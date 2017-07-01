from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from accounts import forms
from django.views.generic import CreateView

#django handels login and logout views
# Create your views here.
class SignUp(CreateView):
    form_class=forms.UserCreateForm
    success_url=reverse_lazy('login')  #not reverse as i want to be executed when they hit submit
    template_name='accounts/signup.html'
