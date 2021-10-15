from django import forms
from django.forms.widgets import EmailInput, TextInput, Textarea
from django.forms import ModelForm
from .models import Comments, Message


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

