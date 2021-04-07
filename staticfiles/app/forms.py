from django import forms

class urlForm(forms.Form):
    url=forms.CharField(max_length=256, widget=forms.TextInput(attrs={'placeholder': 'Enter the URL'}))
