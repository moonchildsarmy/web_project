from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, TextInput, Textarea
from django.forms import ModelForm
from .models import Comments, Message, Order
from django.contrib.auth import authenticate, login


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("text", )


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("full_name", "email", "title", "text")

        widgets = {
            "full_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Email"
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            })
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("count", "size")


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']