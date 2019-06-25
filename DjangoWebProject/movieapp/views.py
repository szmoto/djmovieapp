from django.shortcuts import render
from movieapp.models import Movie

# Create your views here.

def index(request):
    mvs = Movie.objects.all()[:14]
    return render(
        request,
        'movieapp/index.html',
        {'hotmovies':mvs,
            })

def detail(request,pk):
    mv=Movie.objects.get(pk=pk)
    return render(
        request,
        'movieapp/detail.html',
        {'movie':mv,
         })