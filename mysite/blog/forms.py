from django import forms
from django.forms import CharField, Form, PasswordInput

from .models import *
from django.forms import ModelForm






class Writepost_Form(ModelForm):
    class Meta:
        model = Post
        
        exclude = ['user', 'pub_date', 'edit_date']

    def __init__(self, *args, **kwargs):
        super( Writepost_Form, self ).__init__(*args, **kwargs)
        self.fields[ 'tag' ].widget.attrs[ 'placeholder' ]="Tag Name"  
        
