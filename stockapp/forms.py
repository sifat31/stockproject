# stockapp/forms.py
from django import forms
from .models.sql_models import SqlModel

class SqlModelForm(forms.ModelForm):
    class Meta:
        model = SqlModel
        fields = '__all__'
