from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', context={})

def shop(request):
    return render(request, 'shop.html', context={})