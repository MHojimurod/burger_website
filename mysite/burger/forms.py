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


class AboutOurFoodForm(forms.ModelForm):
    class Meta:
        model = AboutOurFood
        fields = '__all__'



class OurblogForm(forms.ModelForm):
    class Meta:
        model = OurBlog
        fields = '__all__'