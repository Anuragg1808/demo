from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.generic import TemplateView
from Website.models import ContactMessage


def index(request):
    return render(request,"TEST_HOME.html",context=None)

def login(request):
    return render(request,"login.html",context=None)

def register(request):
    return render(request,"register.html",context=None)

def about(request):
    return render(request,"about.html",context=None)

def contact(request):
    return render(request,"contact.html",context=None)

def listings(request):
    return render(request,"listings.html",context=None)

def view_property(request):
    return render(request,"view_property.html",context=None)

def book(request):
    return render(request,"book.html",context=None)
         

    

class contact_check(APIView):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        usr = ContactMessage()
        usr.name = name
        usr.email = email
        usr.number = number
        usr.message = message
        usr.save()
        # print(card_id)
        # print(customer_id)
        return JsonResponse({"status": "pass"})
    
class contact_view(TemplateView):
    template_name = "view_contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_data = ContactMessage.objects.all()
        context = { 'userdata': user_data}
        return context
    
class deleteuser2(APIView):
    def post(self, request):
        number = request.POST['number']
        ContactMessage.objects.filter(number = number).delete()
        return JsonResponse({"status": "pass"})