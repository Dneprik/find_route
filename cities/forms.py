from django import forms

from cities.models import City

class HtmlForm(forms.Form):
    name = forms.CharField(label='City')

class CityForm(forms.ModelForm):
    name = forms.CharField(label='To create new city enter name and click "Save"', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter name'
    }))

    class Meta:
        model = City
        fields = ('name', )






