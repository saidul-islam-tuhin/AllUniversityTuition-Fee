from django import forms

class RangeForm(forms.Form):
    min_cost = forms.IntegerField()
    serial = forms.IntegerField(required=False, default='0', widget=forms.TextInput())
