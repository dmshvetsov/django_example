from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Message
        fields = ('name', 'email', 'content')
