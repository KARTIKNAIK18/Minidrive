
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_files)
    
]
