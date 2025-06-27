from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    messages.success(request, "this is a test message")
    return render(request, 'index.html', context)
    
    #return HttpResponse("This is Home Page")

def about(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'about.html', context)

def services(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'services.html', context)

def contacts(request):

    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
        

    context = {
        'variable':"this is sent"
    }
    return render(request, 'contacts.html', context)