from django.shortcuts import render

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            
            movie = Movie.objects.get(user=user.id, movie=movie.id)
            stars = request.data['stars']
            user = request.user
            
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Valutazione aggiornata correttamente', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Valutazione create correttamente', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        
        else:
            response = {'message': 'è necessario fornire il numero di stelle'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
                    
    
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def update(self, request, *args, **kwargs):
        response = {'message': 'None è possibile aggiornare la valutazione con questa modalità.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {'message': 'Non è possibile inserire la valutazione con questa modalità.'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    