from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movie_disp/',views.movie_disp,name='movie_disp'),
    path('register/',views.reg,name='register'),
    path('addreview/',views.add_review,name='add-review'),
    #path('a/',views.import_db,name='importdb'),
    path('demo/',views.demo,name='demo'),
    path('m/',views.products_list,name='disp'),
    path('d/',views.createdata,name='d'),
    path('rec/',views.rec,name='rec'),
    path('m/movies/<slug:id>',views.movies,name='movie'),
    path('user/',views.user,name='users'),
    path('done/',views.done,name='done'),
    path('x/',views.created,name='da'),

]