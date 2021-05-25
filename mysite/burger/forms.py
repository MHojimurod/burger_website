from django import forms
from .models import *



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

