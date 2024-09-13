from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from admindash.models import registeraccount
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def admins(request):
    return render(request,"admindash/admin.html")

def view_users(request):
    return render(request,"admindash/view_users.html")

class login_check(APIView):  
     def post(self, request):
        username = request.POST['username']
        password = request.POST['pass']
        ent = registeraccount.objects.filter(name=username,password=password).values()
        if(len(ent) > 0):
            return JsonResponse({"status":"pass", "name": ent[0]["name"], "role": ent[0]["role"]})
        else:
            return JsonResponse({"status":"fail"})


class register_check(APIView):
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        role = request.POST['role']
        usr = registeraccount()
        usr.name = name
        usr.email = email
        usr.password = password
        usr.cpass = cpass
        usr.role = role
        usr.save()
        # print(card_id)
        # print(customer_id)
        return JsonResponse({"status": "pass"})

from django.views.generic import TemplateView

class register_view(TemplateView):
    template_name = "admindash/view_users.html"

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



@csrf_exempt  # For development/testing purposes; use proper CSRF handling in production
def update_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpass = request.POST.get('cpass')
        old_name = request.POST.get('old_name')  # Use this to find the user to update

        try:
            # Find user by old name
            user = registeraccount.objects.get(name=old_name)
            # Update fields
            user.name = name
            user.email = email
            user.password = password
            user.cpass = cpass
            user.save()
            return JsonResponse({'status': 'success', 'message': 'User updated successfully!'})
        except registeraccount.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found!'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method!'})