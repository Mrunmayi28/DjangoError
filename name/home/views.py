from django.shortcuts import render,HttpResponse
from home.models import Plogins

# Create your views here.
def index(request):
    return render(request,"index.html")
def Plogins(request):
        if request.method=='post':
            Name=request.POST.get('Name')
            Contact=request.POST.get('Contact')
            email=request.POST.get('email')
            Plogins=Plogins(Name=Name  , Contact=Contact , email='email')
            Plogins.save()
            print("Successfully Saved")
        else:
            return render(request,"Plogins.html")

def slogin(request):
    return render(request,"slogin.html")

def spersonalinfo(request):
    return render(request,"spersonalinfo.html")

def academics(request):
    return render(request,"academics.html")
 
def certifications(request):
    return render(request,"certifications.html")

def proctor(request):
    return render(request,"proctor.html")



       



