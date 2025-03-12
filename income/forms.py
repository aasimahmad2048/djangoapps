from django.forms import fields
from .models import Category, Source
from django import forms 



class SourceForm(forms.ModelForm):
      class Meta:
            model=Source
            fields='__all__'

