from django.shortcuts import render
from django.db import models
from .models import Users,Movies,Ratings
# Create your views here.
def index(request):
    return render(request, 'index.html')


def movie_disp(request):
    return render(request, 'movie_disp.html')


def reg(request):
    return render(request, 'register.html')


def add_review(request):
    return render(request, 'add_review')

def import_db(request):
    
    f = open('C:/sh/movies/film/userrate.csv', 'r')  
    for line in f:
        line =  line.split('\t')
        print(line)
        tmp = Ratings(
            user_id = Users.objects.filter(user_id=int(line[0].replace('"',''))).first(),
            movie_id = Movies.objects.filter(movie_id = int(line[1].replace('"',''))).first(),
            rating = line[2]   
        )
        tmp.save()

    f.close()