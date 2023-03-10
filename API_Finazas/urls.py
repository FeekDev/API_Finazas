from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import urls
from finances import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/finanzas', views.finanzas_metodos)
]
