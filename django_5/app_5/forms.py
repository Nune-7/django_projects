from django import forms
from django.forms import ModelForm
from .models import NewTask


class TaskForm(ModelForm):
    class Meta:
        model = NewTask
        fields = '__all__'
        exclude = ['user']
