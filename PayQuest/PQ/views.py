from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,"index.html",{})

def board(request):
    return render(request, "board.html", {})

def checkout_paymentmethod(request):
    return render(request, "checkout_paymentmethod",{})

def contact(request):
    return render(request, "contact.html",{})

def home_page(request):
    return render(request, "home_page.html", {})

def profile(request):
    return render(request, "profile.html", {})

def  susi(request):
    return render(request,"sign_up_sign_in",{})

def tavern(request):
    return render(request, "tavern.html",{})

def DTTS(request):
    return render(request,"DTTS.html", {})