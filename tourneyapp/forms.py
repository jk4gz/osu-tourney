from django import forms

class MapDataForm(forms.Form):
    nm1_link = forms.CharField(required=False)
    nm2_link = forms.CharField(required=False)
