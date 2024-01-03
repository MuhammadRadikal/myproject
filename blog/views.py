from django.shortcuts import render

# Create your views here.
from .models import Artikel

def Home(request):
    List_Artikel = Artikel.objects.all()
    context = {
        'list_artikel' : List_Artikel
    }
    return render(request, 'blog/home.html', context)