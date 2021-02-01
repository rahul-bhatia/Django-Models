from django import forms
class FbForm(forms.Form):
	name=forms.CharField(label="Enter Name")
	feedback=forms.CharField(label="Enter Feedback")