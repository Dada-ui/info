from django import forms
from earnings.models import *


class App_Form(forms.ModelForm):
    class Meta:
        model = App_Model
        fields = '__all__'


class Task_Form(forms.ModelForm):
    class Meta:
        model = Task_Model
        fields = ['screenshot']