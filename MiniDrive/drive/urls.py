
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Get_files),
    path('upload/', views.Post_Files, name = 'upload_file')

    
]
