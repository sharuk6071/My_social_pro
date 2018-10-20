from django.shortcuts import render

# Create your views here.zer



def home(request):
    return render(request,'web_app/home.html')
