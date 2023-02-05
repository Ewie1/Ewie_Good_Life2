from django import forms
from .models import BookTrainer
from datetimepicker.widgets import DateTimePicker


class BookTrainerForm(forms.ModelForm):
    class Meta:
        model = BookTrainer
        fields = ['name', 'date', 'time']
        