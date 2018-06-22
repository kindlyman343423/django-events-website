from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'description', 'image', 'time', 'venue', 'city')
