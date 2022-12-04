"""Form to send messages"""

from django import forms


class MessageForm(forms.Form):
    """_summary_

    Args:
        forms (_type_): _description_
    """
    content = forms.CharField(widget=forms.Textarea, label='Your content')
