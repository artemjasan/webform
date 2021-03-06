from django import forms

from .models import Form


class CreateForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = '__all__'
        labels = {'name': 'Name', 'email': 'E-mail', 'ico': 'IČO'}
