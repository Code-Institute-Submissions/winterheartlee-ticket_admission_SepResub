from django import forms
from .widgets import CustomClearableFileInput
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    starts = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))
    ends = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)