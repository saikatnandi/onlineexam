from django import forms
from django.forms import CharField, Form, PasswordInput
from exam.models import Mcq_Question
from django.forms import ModelForm
	



from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm



class NameForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    password = CharField(widget=PasswordInput())
    email = forms.EmailField(label='Email', max_length=100)


class Mcq_Question_Form(ModelForm):
    class Meta:
        model = Mcq_Question
        exclude = []

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()



class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    birtday = forms.DateField(required = False)



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['Last name']
        user.birthday = self.cleaned_data['Birthday']


        if commit:
            user.save()

        return user