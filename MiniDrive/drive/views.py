from django.shortcuts import render, redirect
import requests
from django.http import JsonResponse
from decouple import config
from django.core.files.storage  import FileSystemStorage
from django.contrib import messages
import base64

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

def Post_Files(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploading_file = request.FILES["file"]

        filedata = base64.b64encode(uploading_file.read()).decode('utf-8')

        payload = {
                "filename":uploading_file.name,
                "filedata": filedata
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(API_URL, json=payload, headers=headers)
            
            if response.status_code == 200:
                messages.success(request,"Files uploded successfully")
            else:
                messages.error(request,f"error occured in uploading file{response.text}")
            
        except Exception as e:
            messages.error(request,f"Upload failed: {str(e)}") 

        return redirect('upload_file')       

    # If it's a GET request or no file was provided
    return render(request, "upload.html")


def Delete_files():
    pass

