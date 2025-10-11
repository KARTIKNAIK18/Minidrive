from django.shortcuts import render, redirect
import requests
from decouple import config
from django.core.files.storage  import FileSystemStorage
from django.contrib import messages

# Create your views here.
API_URL = config("API_URL")
FILE_PATH = ""

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

def Put_Files(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES['file']
        
        # Create a proper multipart/form-data request
        files = {
            'file': (uploaded_file.name, uploaded_file, uploaded_file.content_type)
        }
        
        try:
            # Print debug information
            print(f"Attempting to upload file: {uploaded_file.name}")
            print(f"API URL: {API_URL}")
            
            # Make the request to the API
            response = requests.post(API_URL, files=files)
            
            # Print response details for debugging
            print(f"Response status: {response.status_code}")
            print(f"Response content: {response.text[:200]}...")  # Print first 200 chars
            
            response.raise_for_status()  # Raise an exception for 4XX/5XX responses
            
            # Process successful response
            result = response.json()
            file_url = result.get('url', '#')  # Get the URL from result or use # as fallback
            
            messages.success(request, f'File "{uploaded_file.name}" uploaded successfully!')
            return render(request, "upload.html", {
                "uploaded_file_url": file_url,
                "result": result
            })
        
        except Exception as e:
            print(f"Error uploading file: {e}")
            return render(request, "upload.html", {"error": "Failed to upload file"})
    
    # If it's a GET request or no file was provided
    return render(request, "upload.html")


def Delete_files():
    pass

