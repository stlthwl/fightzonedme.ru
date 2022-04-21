from .models import feedback, message
from django.forms import ModelForm, TextInput, Textarea


class feedbackForm(ModelForm):
    class Meta:
        model = feedback
        fields = ["name", "phone", "txt"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
            "txt": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            })
        }


class messageForm(ModelForm):
    class Meta:
        model = message
        fields = ["name", "phone", "txt"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "txt": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сообщение'
            })
        }
