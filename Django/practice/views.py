from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello home!")


def about(request):
    return HttpResponse("Hello about!")

def contact(request):
    return HttpResponse("Hello contact!")
