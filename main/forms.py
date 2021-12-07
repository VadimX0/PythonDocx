from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from .models import Task, Doc, chkboxcourse
from django import forms

class TaskForm(ModelForm):#Форма ввода для создания заданий
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
         "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
         }),
        }

class DocForm(ModelForm): #Форма ввода для создания документов
    class Meta:
        model = Doc
        fields = ["naming", "name","org"]
        widgets = {"name": TextInput(attrs={
            'class': 'form-control.sm',
            'placeholder': 'Название на латинице'

        }),
            "naming": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваши ФИО'
        }),
            "org": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название организации'
        })
        }



