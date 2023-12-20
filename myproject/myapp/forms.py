from django import forms

class Chatform(forms.Form):
    userquery=forms.CharField(label='Enter Query',max_length=500,required=False, widget=forms.Textarea(attrs={'class': 'centered-textarea', 'placeholder': 'Enter Your Query','rows':'3'}))