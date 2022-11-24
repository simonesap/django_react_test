from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # number_of_ratings e avg_rating sono due funzioni quindi posso richiamare anche funzioni nei serializers
        fields = ('id', 'title', 'description', 'number_of_ratings', 'avg_rating') 
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')