from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movie_disp/',views.movie_disp,name='movie_disp'),
    path('register/',views.reg,name='register'),
    path('addreview/',views.add_review,name='add-review'),
    path('a/',views.import_db,name='importdb'),
]