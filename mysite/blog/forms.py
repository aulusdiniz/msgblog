from django import forms

from .models import Msg

class MsgForm(forms.ModelForm):

    class Meta:
        model = Msg
        fields = ('to', 'text', 'author', 'time')
