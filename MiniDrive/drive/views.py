from django.shortcuts import render
import requests
from decouple import config

# Create your views here.
API_URL = config("API_URL")

# def Home(request):
#     return render(request, 'home.html')


def Get_files(request):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        files = response.json()

    except Exception as e :
        files = []
        print("Error fetching files",e)
    return render(request, "home.html",{"files": files})

def Put_Files():
    pass

def Delete_files():
    pass

