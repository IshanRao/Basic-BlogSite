'''from django import forms

class ContactForm(forms.Form) :

    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=200,widget=forms.Textarea(),help_text='Write your message here')
    #source = forms.CharField(max_length=50,widget=forms.HiddenInput())
    '''

from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm) :

    class Meta :
        model = Contact
        fields = ['name','email','message']