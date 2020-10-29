from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    print(request.POST)
    context = {
        'allshows': Show.objects.all()
        
    }
    
    
    return render(request, "index.html", context)




def new_show(request):

    
    return render(request, "new.html")


def create(request):
    errors= Show.objects.team_create_validate(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release'])
    return redirect("/shows/show")


def view(request, tvid):
    
    tv_info = Show.objects.get(id=tvid)
    
    context = {
        'x': tv_info

    }
    
    return render(request,"showinfo.html", context)

def deleteshow(request, tvid):
    delshow = Show.objects.get(id=tvid)
    delshow.delete()
    
    return redirect("/")


def editshow(request, tvid):
    
    context = {
        "edit": Show.objects.get(id=tvid)
    }
    
    return render(request,"editform.html", context)

def updateshow(request, tvid):
                
        u = Show.objects.get(id=tvid)
        
        u.title= request.POST['title']
        u.network= request.POST['network']
        u.release_date= request.POST['release']
        u.save()
        
        

        return redirect("/")
