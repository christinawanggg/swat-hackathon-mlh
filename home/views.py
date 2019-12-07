from django.shortcuts import render

from .models import Home

# Create your views here.
def home(request):
    jobs = Home.objects
    return render(request, 'symptoms/home.html', {'symptoms':home})
