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
    hr1_link = forms.URLField(required=False, label='HR1', widget=forms.URLInput(attrs={'size': '50'}))
    hr2_link = forms.URLField(required=False, label='HR2', widget=forms.URLInput(attrs={'size': '50'}))
    hr3_link = forms.URLField(required=False, label='HR3', widget=forms.URLInput(attrs={'size': '50'}))
    dt1_link = forms.URLField(required=False, label='DT1', widget=forms.URLInput(attrs={'size': '50'}))
    dt2_link = forms.URLField(required=False, label='DT2', widget=forms.URLInput(attrs={'size': '50'}))
    dt3_link = forms.URLField(required=False, label='DT3', widget=forms.URLInput(attrs={'size': '50'}))
    dt4_link = forms.URLField(required=False, label='DT4', widget=forms.URLInput(attrs={'size': '50'}))
    fm1_link = forms.URLField(required=False, label='FM1', widget=forms.URLInput(attrs={'size': '50'}))
    fm2_link = forms.URLField(required=False, label='FM2', widget=forms.URLInput(attrs={'size': '50'}))
    fm3_link = forms.URLField(required=False, label='FM3', widget=forms.URLInput(attrs={'size': '50'}))
    tb_link = forms.URLField(required=False, label='TB', widget=forms.URLInput(attrs={'size': '50'}))
