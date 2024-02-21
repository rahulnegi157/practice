from django.shortcuts import render
from .models import Register
# Create your views here.

def home(request):
    mydata=Register.objects.all()
    return render(request,'app/index.html',{'data':mydata})

def savedata(request):
    name=request.POST['name']
    city=request.POST['city']
    email=request.POST['email']
    Register.objects.create(name=name,
                            city=city,
                            email=email)
    mydata=Register.objects.all()
    return render(request,'app/index.html',{'data':mydata})

def deletedata(request,rahul):
    Register.objects.get(id=rahul).delete()
    mydata=Register.objects.all()
    return render(request,'app/index.html',{'data':mydata})

def editdata(request,rahul):
    updatedata=Register.objects.get(id=rahul)
    mydata=Register.objects.all()
    return render(request,'app/index.html',{'data':mydata,
                                            'updateform':'mydata',
                                            'update':updatedata})