from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from home.models import Home
def index(request):
    Data = {
            'Homes':Home.objects.all()
        } 
    return render(request,'page/home.html',Data)

def home(request):
    Data = {
            'Homes':Home.objects.all()
        } 
    return render(request,'page/home.html',Data)
 
def contact(request):
    return render(request,'page/contact.html')

def register(request):
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            return HttpResponseRedirect("/")
        return render(request,'page/register.html',{'form':form })
    form = RegistationForm()
    return render(request,'page/register.html',{'form':form })

def posttc(request, post_id): 
    return render(request,'page/posttc.html',{'home':Home.objects.get(pk=post_id)})
