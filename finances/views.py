from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello people, welcome in your finances')