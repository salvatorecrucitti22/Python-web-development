from django.shortcuts import render
from django.shortcuts import HttpResponse
'''def index(request):
    return HttpResponse('<h1>Initial Page</h1>')'''

def home(request):
    return render(request, 'index.html')