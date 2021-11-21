from django import forms

class EmployeerForm(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=15)
