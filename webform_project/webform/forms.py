from django import forms
from django.core.validators import validate_email

from .ico_validation import ico_exists
from .models import Form


class CreateForm(forms.ModelForm):

    class Meta:
        model = Form
        fields = '__all__'
        labels = {'name': 'Name', 'email': 'E-mail', 'ico': 'IČO'}
