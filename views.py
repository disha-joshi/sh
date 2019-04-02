from django.shortcuts import render
from django.db import models
from .import predictor 
from .models import Users,Movies,Ratings,Info
# Create your views here.
def index(request):
    return render(request, 'index.html')


def movie_disp(request):
    return render(request, 'movie_disp.html')


def reg(request):
    return render(request, 'register.html')


def add_review(request):
    return render(request, 'add_review.html')

def rec(request):
    return render(request, 'recom.html')    

def done(request):
    return render(request, 'done.html')    

    


#def import_db(request):
    
 #   f = open('C:/sh/movies/film/userrate.csv', 'r')  
  #  for line in f:
   #     line =  line.split('\t')
    #    print(line)
     #   tmp = Ratings(
      #      user_id = Users.objects.filter(user_id=int(line[0].replace('"',''))).first(),
       #     movie_id = Movies.objects.filter(movie_id = int(line[1].replace('"',''))).first(),
        #    rating = line[2]   
        #)
        #tmp.save()

    #f.close()

 
def demo(request):
    return render(request, 'demo.html')

def products_list(request):
    products = Movies.objects.all()[0:10]
    print(products)
    return render(request, 'movie_disp.html', \
         context={'movie_disp': products})

    


def createdata(request):
        if request.method == 'GET':
            if request.GET.get('username') and request.GET.get('name') and request.GET.get('email') and request.GET.get('password') :
                post=Info()
                post.username= request.GET.get('username')
                post.name= request.GET.get('name')
                post.email= request.GET.get('email')
                post.password= request.GET.get('password')
                post.save()
                
                return render(request, 'demo.html')  

        else:
                return render(request,'demo.html')


def movies(request,id):
        x = predictor.similarityPredictionItem(predictor.item_similarity)
        print()
        listed = []
        listed = x[id]
        m = []
        print(listed)
        for i in listed:   
            m.append(predictor.items.loc[i-1]['movie_title'])
        return render(request, 'recom.html', context={'movies': m})

def created(request):
        if request.method == 'POST':
            data = request.POST.get('userid')
            response = user(request,data)
                #post=Users()
                #post.user_id= request.GET.get('userid')
            return response
                
        else:
            return render(request, 'userrec.html') 


def user(request,id):
        #response = created('request')
        x = predictor.similarityPrediction(predictor.user_similarity)
        print()
        y = {}
        y = predictor.predictUserMovie(id)
        print(y)
        # listed = []
        # listed = x[id]
        # m = []
        # print(listed)
        # #for i in listed:   
        # m.append(predictor.items.loc[id]['movie_title'])
        return render(request, 'userrec.html', context={'user': y})


