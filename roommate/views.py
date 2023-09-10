from django.shortcuts import render

# Create your views here.

def roommate(request):
    return render(request,'index.html')
