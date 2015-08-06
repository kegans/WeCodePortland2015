from django.shortcuts import render
from .models import PostUser


# Create your views here.
def profile(request):
    return render(request, 'wecodeapp/profile.html', {})

def mosaic(request):
    return render(request, 'wecodeapp/hackathon.html', {})
