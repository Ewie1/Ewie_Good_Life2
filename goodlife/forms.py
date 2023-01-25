from django import forms
from .models import BookTrainer


class BookTrainerForm(forms.ModelForm):
    class Meta:
        model = BookTrainer
        fields = '__all__'
       