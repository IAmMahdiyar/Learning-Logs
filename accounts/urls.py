from django.contrib import admin
from django.urls import path, include
from .views import sign_up
app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', sign_up)
]
