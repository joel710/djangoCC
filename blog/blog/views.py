from django.http import HttpResponse
from django.shortcuts import render

def home_views(request):
    # return HttpResponse('hello world')
    return render(request, 'home.html')

def contact_views(request):
    # return HttpResponse('Contactez nous')
    return render(request, 'contact.html')

def article_views(request):
    # return HttpResponse('Contactez nous')
    return render(request, 'article.html')