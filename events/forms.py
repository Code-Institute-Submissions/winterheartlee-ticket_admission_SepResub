from django import forms
from .widgets import CustomClearableFileInput
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    # using attrs to send type:datetime-local for HTML5 datetime picker
    starts = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
    ends = forms.DateTimeField(
        input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
    user = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'type': 'hidden'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
