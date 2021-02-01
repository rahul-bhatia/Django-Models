from django import forms

class RaInputF(forms.Form):
	name=forms.CharField()
	options=forms.ChoiceField(choices=[('django','django'),('express','express'),('laravel','laravel')])