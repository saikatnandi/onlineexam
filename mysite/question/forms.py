from django import forms
from django.forms import CharField, Form, PasswordInput

from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from readingmaterial.models import *

from django.forms import ModelForm
from decimal import Decimal




class ExcelForm2(ModelForm):
	class Meta:
		model = Upload_Question_From_Excel
		exclude = ['pub_date', 'edit_date']


class Upload_Question_Set_From_Excel_Form(ModelForm):
    class Meta:
        model = Upload_Question_Set_From_Excel
        exclude = ['pub_date', 'edit_date']






class create_question_topic_wise_form(forms.Form):
    question_topic = forms.ModelChoiceField(queryset=Question_Topic.objects.all(), label="Select Topic For This Question")
    question_title = forms.CharField(max_length=100)
    total_question = forms.IntegerField(initial=0, required=True)

    marks = forms.IntegerField(initial=1, required=True, label="Individual Question Marks")
    negative_marks = forms.IntegerField(initial=25, required=True,
     label="How Percent Marks Will Be Deducted For Wrong Answer: ")

    topic_list = forms.ModelMultipleChoiceField(queryset=ReadingTopic.objects.all(), widget  = forms.CheckboxSelectMultiple)

    # profile = forms.ModelChoiceField(queryset=Profile.objects.all(),
    #         widget=forms.HiddenInput())


class create_question_sub_topic_wise_form(forms.Form):
    question_title = forms.CharField(max_length=100)
    # total_question = forms.IntegerField(initial=0, required=True)

    marks = forms.IntegerField(initial=1, required=True, label="Individual Question Marks")
    negative_marks = forms.IntegerField(initial=25, required=True,
    label="How Percent Marks Will Be Deducted For Wrong Answer: ")

    # topic_list = forms.ModelChoiceField(queryset=ReadingTopic.objects.all())

    sub_topic_list = forms.ModelMultipleChoiceField(queryset=SubTopic1.objects.all(), widget  = forms.CheckboxSelectMultiple)
