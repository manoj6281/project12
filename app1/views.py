from django.shortcuts import render

# Create your views here.

def manu(request):
    return render(request,'manu.html')