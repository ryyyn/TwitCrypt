from django import forms

#from .models import


class MessageForm(forms.Form):
    message = forms.CharField(label="message", max_length=140)

    #class Meta:
    #    model = Contact

