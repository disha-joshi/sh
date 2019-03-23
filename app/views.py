from django.shortcuts import render
from django.db import models
from .models import Users
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
    
    f = open('C:/sh/movies/cinema/user.csv', 'r')  
    for line in f:
        line =  line.split('|')
        print(line)
        tmp = Users(
            user_id = int(line[0].replace('"', '')),
            age = line[1],
            sex = line[2],
            occupation = line[3],
            zip_code = int(line[4].replace('"', ''))
        )
        tmp.save()

    f.close()