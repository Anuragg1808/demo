from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from Website.models import registeraccount

def index(request):
    return render(request,"TEST_HOME.html",context=None)

def login(request):
    return render(request,"login.html",context=None)

def register(request):
    return render(request,"register.html",context=None)

def about(request):
    return render(request,"about.html",context=None)

class login_check(APIView):  
     def post(self, request):
         username = request.POST['username']
         password = request.POST['pass']
         if username == 'test':
            return JsonResponse({"status":"pass"})
         else:
             return JsonResponse({"status":"fail"})
         

class register_check(APIView):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        usr = registeraccount()
        usr.name = name
        usr.email = email
        usr.password = password
        usr.cpass = cpass
        usr.save()
        # print(card_id)
        # print(customer_id)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class register_view(TemplateView):
    template_name = "view_register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = registeraccount.objects.all()
        context = { 'userdata': user_data}
        return context
    
class deleteuser(APIView):
    def post(self, request):
        name = request.POST['name']
        registeraccount.objects.filter(name = name).delete()
        return JsonResponse({"status": "pass"})