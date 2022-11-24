from django.contrib import admin

from .models import Movie, Rating
# from user.models import User

# admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)