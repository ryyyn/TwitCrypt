from django import forms
from crypto.models import CodeRecord


class CodeRecordForm(forms.ModelForm):
    class Meta:
        model = CodeRecord
        fields = ['code', 'password'] # and not 'otp', 'exp_time'
        widgets = {
            'password': forms.PasswordInput()
        }


class ValidateForm(forms.Form):
    code = forms.CharField(label='Coded message', max_length=140)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput()
    }

