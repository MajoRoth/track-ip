from django.shortcuts import render
from scripts.ipgen import get_ip
# Create your views here.


def home(request):
    get_ip(request)
    return render(request, 'index.html')




