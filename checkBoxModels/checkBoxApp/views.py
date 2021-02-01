from django.shortcuts import render
from .forms import MaForm
from .models import MaModel
# Create your views here.
def home(request):
	fm=MaForm()
	if request.method=="POST":
		na=request.POST.get('name')
		n=request.POST.get('notes')
		s=request.POST.get('software')
		c=request.POST.get('certi')
		print(na,n,s,c)
		n=False if n is None else n
		s=False if s is None else s
		c=False if c is None else c
		ma=MaModel(name=na,notes=n,software=s,certi=c)
		ma.save()
		return render(request,'home.html',{'fm':fm,'msg':"Thanks "+na+" Bon Voyage!"})	
	return render(request,'home.html',{'fm':fm})
