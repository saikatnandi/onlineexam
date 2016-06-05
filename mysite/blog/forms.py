from django import forms
from django.forms import CharField, Form, PasswordInput

from .models import *
from django.forms import ModelForm
from ckeditor.widgets import *
from ckeditor.fields import *
from ckeditor_uploader.fields import *



class Writepost_Form(ModelForm):
    # title = forms.CharField(widget=CKEditorWidget())
    # title2 = forms.CharField()

    class Meta:
        model = Post
        
        exclude = ['user', 'pub_date', 'edit_date']

        widgets = {
            'title_text': CKEditorWidget(),
            'tag': forms.CheckboxSelectMultiple,
            # 'title2':  CKEditorWidget(),
        }

    # def get_initial(self):
    #     # call super if needed
    #     return {'fieldname': somevalue}

    def __init__(self, *args, **kwargs):
        super( Writepost_Form, self ).__init__(*args, **kwargs)
        # super(Writepost_Form, self).__init__(request=request, *args, **kwargs)
        # fields_keyOrder = [
        #     'title',
        #     'post_body',
        #     'image1',
        #     'image2',
        #     'image3',
        #     'tag'
        #     ]
        # if (self.fields.has_key('keyOrder')):
        #     self.fields.keyOrder = fields_key_order
        # else:
        #     self.fields = OrderedDict((k, self.fields[k]) for k in fields_key_order)

        self.fields[ 'tag' ].widget.attrs[ 'placeholder' ]="Tag Name"  
