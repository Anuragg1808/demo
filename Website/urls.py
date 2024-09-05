
from django.urls import path

from Website import views

urlpatterns = [
        path('',views.index,name='index'),
        path('login',views.login,name='login'),
        path('register',views.register,name='register'),
        path('about/',views.about,name='about'),
        path('contact',views.contact,name='contact'),
        path("login_check", views.login_check.as_view(), name='login_check'),

        path("register_check",views.register_check.as_view(),name="register_check"),
        path("register_view",views.register_view.as_view(),name="register_view"),
        path("contact_check",views.contact_check.as_view(),name="contact_check"),
        path("contact_view",views.contact_view.as_view(),name="contact_view"),
        path("deleteuser",views.deleteuser.as_view(),name="deleteuser"),
        path("deleteuser2",views.deleteuser2.as_view(),name="deleteuser2")
    ]