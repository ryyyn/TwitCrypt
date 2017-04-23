from django import forms
from crypto.models import CodeRecord


class CodeRecordForm(forms.ModelForm):
    class Meta:
        model = CodeRecord
        fields = ['code', 'password'] #and not 'otp', 'exp_time'



