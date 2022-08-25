from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request,"home.html")

def causes(request):
    return render(request,"causes.html")

def mythsfacts(request):
    return render(request,"mythsfacts.html")

def prevention(request):
    return render(request,"prevention.html")

def types(request):
    return render(request,"types.html")

def quizes(request):
    return render(request,"quizes.html")

def products(request):
    queryset = Product.objects.all()
    context = {"products": queryset}
    return render(request,"products.html",context=context)

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def profile(request):
    return render(request,"profile.html")

def quiz(request):
    return render(request,"quiz.html")

def finishedquiz(request):
    return render(request,"finishedquiz.html")


def logedout(request):
    return render(request,"logedout.html")


