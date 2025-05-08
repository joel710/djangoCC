from django.http import HttpResponse

def home_views(request):
    return HttpResponse('hello world')


def contact_views(request):
    return HttpResponse('Contactez nous')