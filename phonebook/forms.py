
from django import forms
from .models import ContactInfo

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        exclude = ('user',)
