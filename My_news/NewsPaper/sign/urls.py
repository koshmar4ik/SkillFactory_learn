from django.contrib import admin
from django.urls import path, include
from .views import IndexView, BaseRegisterView, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('login/',
         LoginView.as_view(template_name='accounting/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='accounting/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='accounting/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
]