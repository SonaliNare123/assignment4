from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('Addpage', views.Addpage,name="Addpage"),
    path('Recordpage', views.Recordpage,name="Recordpage"),
    path('check',views.getdata,name="getdata"),
]
