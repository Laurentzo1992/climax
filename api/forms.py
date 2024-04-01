# Dans forms.py
# Dans forms.py
from django import forms
from .models import Employee

class UploadFileForm(forms.Form):
    file = forms.FileField()

