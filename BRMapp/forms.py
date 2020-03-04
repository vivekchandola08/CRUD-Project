from django import forms

class NewBookform(forms.Form):
    title=forms.CharField(label='title',max_length=100)
    price=forms.FloatField(label='price')
    author=forms.CharField(label='author',max_length=100)
    publisher=forms.CharField(label='publisher',max_length=100)
class searchform(forms.Form):
    title=forms.CharField(label='title',max_length=100)
