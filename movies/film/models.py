from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.IntegerField(default=0)
    age = models.IntegerField(default=0)    
    sex = models.TextField()
    occupation = models.CharField(max_length=255)
    #zip_code = models.CharField(max_length = 255)
    


class Movies(models.Model):
    movie_id = models.IntegerField(default=0)
    movie_title = models.CharField(max_length=255)
    #release_date = models.DateField()
    #video_release_date = models.DateField()
    Imdb_url = models.CharField(max_length=255)
    unknown = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    film_noir = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    musical = models.IntegerField(default=0)
    mystery = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    sci_fi = models.IntegerField(default=0)
    thriller = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    western = models.IntegerField(default=0)

class Ratings(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE, null = True)
    rating = models.IntegerField(default=0)
    #unix_timestamp = models.TimeField(default=0)
