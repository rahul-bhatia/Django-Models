from django.shortcuts import render
from .forms import EnForm
from .models import EnModel
# Create your views here.
def home(request):
	if request.method=="POST":
		n=request.POST.get('name')
		e=request.POST.get('email')
		p=request.POST.get('phone')
		print(n,e,p)
		d=EnModel(name=n,email=e,phone=p)
		d.save()
		fm=EnForm()
		return render(request,'home.html',{'fm':fm,'msg':"Thanks for feedback! we will revert asap"})
	fm=EnForm()
	return render(request,'home.html',{'fm':fm})