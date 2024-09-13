from django.urls import path
from admindash import views

urlpatterns = [
        path('',views.admins,name='admins'),
        path('view_users',views.view_users,name='view_users'),

        path("login_check", views.login_check.as_view(), name='login_check'),

        path('register_check',views.register_check.as_view(),name='register_check'),
        path('register_view',views.register_view.as_view(),name='register_view'),

        path("deleteuser",views.deleteuser.as_view(),name="deleteuser"),

         path('updateuser',views.update_user, name='update_user'),
]
