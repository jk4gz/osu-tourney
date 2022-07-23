from turtle import width
from xml.dom.minidom import Attr
from django import forms

class MapDataForm(forms.Form):
    nm1_link = forms.URLField(required=False, label='NM1', widget=forms.URLInput(attrs={'size': '50'}))
    nm2_link = forms.URLField(required=False, label='NM2', widget=forms.URLInput(attrs={'size': '50'}))
    nm3_link = forms.URLField(required=False, label='NM3', widget=forms.URLInput(attrs={'size': '50'}))
    nm4_link = forms.URLField(required=False, label='NM4', widget=forms.URLInput(attrs={'size': '50'}))
    nm5_link = forms.URLField(required=False, label='NM5', widget=forms.URLInput(attrs={'size': '50'}))
    nm6_link = forms.URLField(required=False, label='NM6', widget=forms.URLInput(attrs={'size': '50'}))
    hd1_link = forms.URLField(required=False, label='HD1', widget=forms.URLInput(attrs={'size': '50'}))
    hd2_link = forms.URLField(required=False, label='HD2', widget=forms.URLInput(attrs={'size': '50'}))
    hd3_link = forms.URLField(required=False, label='HD3', widget=forms.URLInput(attrs={'size': '50'}))
