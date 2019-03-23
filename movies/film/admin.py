from django.contrib import admin
from .models import Users, Ratings, Movies

# Register your models here.


admin.site.register(Users)
admin.site.register(Ratings)
admin.site.register(Movies)