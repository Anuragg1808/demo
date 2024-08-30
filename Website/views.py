from django.shortcuts import render

def index(request):
    return render(request,"TEST_HOME.html",context=None)

def login(request):
    return render(request,"login.html",context=None)

def register(request):
    return render(request,"register.html",context=None)