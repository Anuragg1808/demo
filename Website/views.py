from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

def index(request):
    return render(request,"TEST_HOME.html",context=None)

def login(request):
    return render(request,"login.html",context=None)

def register(request):
    return render(request,"register.html",context=None)

class login_check(APIView):  
     def post(self, request):
         username = request.POST['username']
         password = request.POST['pass']
         if username == 'test':
            return JsonResponse({"status":"pass"})
         else:
             return JsonResponse({"status":"fail"})