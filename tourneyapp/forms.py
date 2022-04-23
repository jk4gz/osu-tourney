from django import forms

class MapDataForm(forms.Form):
    map_link = forms.DateField(help_text="Enter a beatmap link :D")
