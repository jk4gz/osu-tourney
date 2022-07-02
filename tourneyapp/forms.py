from django import forms

class MapDataForm(forms.Form):
    nm1_link = forms.URLField(required=False)
    nm2_link = forms.URLField(required=False)
