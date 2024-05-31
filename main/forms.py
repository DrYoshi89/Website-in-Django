from cProfile import label
from logging import PlaceHolder
from unittest.util import _MAX_LENGTH
from xml.dom.minidom import Attr
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input1 border-3', 'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Email'}))
    Subject = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input1', 'placeholder': 'Subject'}))
    Message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'input1', 'placeholder': 'Message'}))