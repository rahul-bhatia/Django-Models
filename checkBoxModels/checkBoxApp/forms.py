from django import forms

class MaForm(forms.Form):
	name=forms.CharField()
	notes=forms.BooleanField(required=False)
	software=forms.BooleanField(required=False)
	certi=forms.BooleanField(required=False)