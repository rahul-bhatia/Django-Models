from django.shortcuts import render
from .form import FbForm
from .models import FbModel

# Create your views here.
def home(request):
	fm=FbForm()
	if request.method=="POST":
		n=request.POST.get('name')
		fb=request.POST.get('feedback')
		print(n,fb)
		d=FbModel(name=n,feedback=fb)
		d.save()
		return render(request,'home.html',{'fm':fm,'msg':'Thanks for your feedback'})	
	return render(request,'home.html',{'fm':fm})