from django.shortcuts import render

# Create your views here.
from .models import About

def about_page(request):
    about = About.objects.first()
    return render(request, 'about/about_page.html', {'about': about})