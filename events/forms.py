from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    time = forms.DateTimeField(input_formats=['%Y-%m-%dT0%H:%M'],
                               widget=forms.
                               DateTimeInput(attrs={'type': 'datetime-local',
                                                    'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ('name', 'description', 'image', 'time', 'venue', 'city')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }
