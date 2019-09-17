from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Rating, Genre, Actor
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, MovieSerializer, RatingSerializer, MovieDetailSerializer, ActorSerializer
from django.contrib.auth.decorators import login_required
from .forms import RatingForm
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk= movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@login_required  
@api_view(['POST'])
def rating_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk= movie_pk)
    serializer = RatingSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)
        return Response({'message': '작성되었습니다'})

@login_required
@api_view(['PUT','DELETE'])
def rating_update_and_delete(request, rating_pk, movie_pk):
    rating = get_object_or_404(Rating, pk = rating_pk)
    if request.method == 'PUT':
        serializer = RatingSerializer(data= request.data, instance=rating)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다'})
    else:
        # 작성자와 동일한지 확인해보고 삭제시켜줘
        score.delete()
        return Response({'message': '삭제되었습니다.'})
    
@require_POST
@login_required  
def create_rating(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if len(movie.rating_set.filter(user_id = request.user.id)) == 0:
        ratingform = RatingForm(request.POST)
        if ratingform.is_valid():
            rating = ratingform.save(commit=False)
            rating.user = request.user
            rating.movie_id = movie_pk
            rating.save()
        return redirect('page:detail', movie_pk)
    else:
        return redirect('page:detail', movie.pk)
        
@login_required
def rating_update(request, movie_pk, rating_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rating = get_object_or_404(Rating, pk=rating_pk)
    if rating.user != request.user:
        return redirect('page:list')

    if request.method == 'POST':
            ratingform = RatingForm(request.POST, instance=rating)
            if ratingform.is_valid():
                rating.save()
                return redirect('page:detail', movie.pk)
    else:
       ratingform = RatingForm(instance=rating)
    context = {
        'ratingform':ratingform
    }
    return render(request, 'page/form.html', context)


        
@login_required
def delete_rating(request, movie_pk, rating_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    rating = get_object_or_404(Rating, pk=rating_pk)
    if request.method == 'POST':
        rating.delete()
    return redirect('page:detail', movie.pk)
    