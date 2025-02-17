from django.contrib import admin
from django.urls import path
from aquanet import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name="login"),
    path('logout/',views.Logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('trackdata/',views.trackdata,name='trackdata'),
    path('register_user/',views.new_user,name="new_user"),
    path('collect_data/',views.collect_data,name="collect_data"),
    path('email_alert/',views.email_alert,name="email_alert"),
    path('message_alert/',views.message_alert,name="message_alert"),
    path('getData/',views.getData,name="getData"),
]