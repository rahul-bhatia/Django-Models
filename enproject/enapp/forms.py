from django import forms
class EnForm(forms.Form):
	name=forms.CharField(label="Enter Name")
	email=forms.EmailField(label="Enter Email")
	phone=forms.CharField(label="Enter phone number")