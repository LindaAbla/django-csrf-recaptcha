from django.contrib import admin
from django.urls import path, include

from account.views import (
    sing_in, sing_up, dashboard, log_out, admin_d
)
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login', sing_in, name='sing_in'),
    path('register', sing_up, name='sing_up'),
    path('logout', log_out, name='log_out'),
    path('admin', admin_d, name='admin'),
    
]
