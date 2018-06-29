from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello!")


def json(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return JsonResponse({'STATUS': ip})

def login(request):
    return render(request, 'login/login.html')
