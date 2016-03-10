from django import forms
from django.forms import CharField, Form, PasswordInput
from exam.models import Mcq_Question
from .models import *

from django.forms import ModelForm



class Mcq_Question_Form(ModelForm):
    class Meta:
        model = Mcq_Question
        exclude = []

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


# class ImageForm(ModelForm):
# 	class Meta:
# 		model=Image
# 		exclude=[]

class ExcelForm(forms.Form):
	file = forms.FileField()


# class ExcelForm(ModelForm):
# 	class Meta:
# 		model = Upload_Question_From_Excel
# 		exclude = []
