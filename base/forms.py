from django.forms import Form, CharField, TextInput, ModelForm,PasswordInput
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class SignUpForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}), label=False)
    email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}), label=False)
    password1 = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}), label=False)
    password2 = CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm password'}), label=False)
    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2' )
        
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
     
class PostForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'placeholder': 'Name'}), label=False)
    description =  CharField(widget=TextInput(attrs={'placeholder': 'Description'}), label=False)
    email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}), label=False)
    class Meta:
        model=Post
        fields='__all__'
        fields = ['name', 'description', 'email']
        
