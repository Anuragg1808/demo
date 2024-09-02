
from django.urls import path

from Website import views

urlpatterns = [
        path('',views.index,name='index'),
        path('login',views.login,name='login'),
        path('register',views.register,name='register'),
        path("login_check",views.login_check.as_view(),name='login_check'),
    ]
