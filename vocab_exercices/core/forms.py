from django import forms
from .models import Lemme


class YourModelForm(forms.ModelForm):
    class Meta:
        model = Lemme
        fields = '__all__'  # Use '__all__' to include all fields from the model
