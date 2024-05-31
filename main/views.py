from tkinter.tix import Form
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def index(response): 
    return render(response, "main/base.html", {})

def home(response): 
    return render(response, "main/home.html", {})

def about(response): 
    return render(response, "main/about.html", {})
    
def portfolio(response): 
    return render(response, "main/portfolio.html", {})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            t = form.cleaned_data["subject"]
            m = form.cleaned_data["Message"]
            
            send_mail(
                "Website Email from" + n + t, #Subject
                m, #Message
                e, #Email Sender
                [ 'dac220809@gmail.com'], #Email recipiente
            )
    
    else:
        form = ContactForm()
    return render(request, "main/contact.html", {"form":form})