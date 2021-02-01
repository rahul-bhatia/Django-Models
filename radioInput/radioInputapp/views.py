from django.shortcuts import render
from .form import RaInputF
from .models import RaInput

# Create your views here.
def home(request):
	if request.method=='POST':
		fm=RaInputF()
		n=request.POST.get('name')
		o=request.POST.get('options')
		print(n,o)
		fb=RaInput(name=n,options=o)
		fb.save()
		return render(request,'home.html',{'fm':fm,'msg':'Thanks! '+o+' rocks'})	
	else:
		fm=RaInputF()
		return render(request,'home.html',{'fm':fm})