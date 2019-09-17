from rest_framework import serializers
from .models import Movie, Rating, Genre, Actor

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'genre_box_id']
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'actor_name', 'actor_id']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'comment', 'score', 'movie_id', 'user_id']

class MovieSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'rating_set', 'adult', 'budget', 'genres', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'revenue', 'runtime', 'tagline', 'title', 'actor_1', 'actor_2', 'actor_3', 'director', 'file_path_1', 'file_path_2', 'file_path_3',]

 
class MovieDetailSerializer(serializers.ModelSerializer):
    rating_set = RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'rating_set', 'adult', 'budget', 'genres', 'original_title', 'overview', 'popularity', 'poster_path', 'release_date', 'revenue', 'runtime', 'tagline', 'title', 'actor_1', 'actor_2', 'actor_3', 'director', 'file_path_1', 'file_path_2', 'file_path_3',]
    
    