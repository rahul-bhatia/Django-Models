from django import forms

class RaInputF(forms.Form):
	name=forms.CharField()
	options=forms.ChoiceField(widget=forms.RadioSelect,choices=[('django','django'),('express','express'),('laravel','laravel')])