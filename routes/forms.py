from django import forms

from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):

    from_city =forms.ModelChoiceField(label="From city", queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single',
        'title': 'Please select an item from this list',
        'oninvalid': "setCustomValidity('Please select an item from this list')",
        'oninput': "setCustomValidity('')"
    }))

    to_city = forms.ModelChoiceField(label='To city', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single',
        'title': 'Please select an item from this list',
        'oninvalid': "setCustomValidity('Please select an item from this list')",
        'oninput': "setCustomValidity('')"
    }))

    cities = forms.ModelMultipleChoiceField(label='Through cities (optional)', queryset=City.objects.all(), required=False,
                                            widget=forms.SelectMultiple(attrs={
        'class': 'form-control js-example-basic-multiple',
        'placeholder': 'Optional',
        }
    ))

    travelling_time = forms.IntegerField(label='Time in travel (optional)', required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Optional',
        'title': 'Please enter time in travel',
        'oninvalid': "setCustomValidity('Please enter time in travel')",
        'oninput': "setCustomValidity('')"
    }))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label='Name of route',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name of route'}))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())

    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())

    trains = forms.ModelMultipleChoiceField(queryset=Train.objects.all(), required=False,
                                            widget=forms.SelectMultiple(attrs={'class': 'form-control d-none'}))

    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = '__all__'
