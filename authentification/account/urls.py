from django.contrib import admin
from django.urls import path, include

from account.views import (
    sing_in, sing_up, dashboard, log_out, admin_d, help, captcha, signin, dashboardd
)
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('logout', log_out, name='log_out'),
    path('admin', admin_d, name='admin'),
    path('help', help, name='help'),
    path('captcha', captcha, name='captcha'),
    path('signin', signin, name='signin'),
    path('dashboard', dashboardd, name='dashboardd'),
    
]
