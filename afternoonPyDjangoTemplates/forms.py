from django import forms


class ContactForm(forms.Form):
    location = forms.CharField()
    email = forms.CharField()
    call = forms.CharField()