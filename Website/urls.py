
from django.urls import path

from Website import views

urlpatterns = [
        path('',views.index,name='index'),
        path('login',views.login,name='login'),
        path('register',views.register,name='register'),
        path('about/',views.about,name='about'),
        path('contact',views.contact,name='contact'),
        path('view_property',views.view_property,name='view_property'),
        path('book',views.book,name='book'),
        path('listings',views.listings,name='listings'),
        path("contact_check",views.contact_check.as_view(),name="contact_check"),
        path("contact_view",views.contact_view.as_view(),name="contact_view"),
        
        path("deleteuser2",views.deleteuser2.as_view(),name="deleteuser2")
    ]