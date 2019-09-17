from django.shortcuts import render, get_object_or_404
from posts.models import Movie, Rating, Genre, Actor
from posts.forms import RatingForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def main(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    keyword = request.GET.get('keyword', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if keyword: # q가 있으면
       movies = movies.filter(title__icontains=keyword) # 제목에 q가 포함되어 있는 레코드만 필터링
    context = {
            'genres':genres,
            'movies':movies,
        }
    return render(request, 'page/main.html', context)

@login_required  
def list(request):
    movies = Movie.objects.all()[:10]
    genres = Genre.objects.all()
    genre_name_arr = [0]*21
    favorite = [0]*21
    genre_arr = [0]*21
    ratings = request.user.rating_set.all
    if ratings():
        for rating in ratings():
            for genre in genres:
                
                if genre.genre_box_id == rating.movie.genres:
                    favorite[genre.id] += 1
                    genre_arr[genre.id] = int(genre.genre_box_id)
                    genre_name_arr[genre.id] = genre.name
        max_vote = favorite.index(max(favorite))
        like_genre = genre_name_arr[max_vote]
    
        favorite_genres = Movie.objects.filter(genres=genre_arr[max_vote]).all()[:10]
    budgets = Movie.objects.filter(~Q(budget='N/A')).filter(budget__contains='00000000')[:10]
    if ratings():
        context = {
            'genres':genres,
            'ratings':ratings,
            'movies':movies,
            'budgets':budgets,
            'favorite_genres':favorite_genres,
            'like_genre' : like_genre,
        }
    else:
         context = {
            'genres':genres,
            'movies':movies,
            'budgets':budgets,
        }
         
    return render(request, 'page/list.html', context)

@login_required
def genre(request, genre_pk):
    movies = Movie.objects.all()
    keyword = request.GET.get('keyword', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if keyword: # q가 있으면
       movies = movies.filter(title__icontains=keyword) # 제목에 q가 포함되어 있는 레코드만 필터링
    context = {
        'movies':movies,
        'genre_pk':genre_pk
    }
    return render(request, 'page/genre.html', context)

@login_required    
def detail(request, movie_pk):
    actors_1 = Actor.objects.all()
    actor_name_arr = []
    actors = []
    for i in actors_1:
        if i.actor_name not in actor_name_arr:
            actors.append(i)
            actor_name_arr.append(i.actor_name)
    genres = Genre.objects.all()
    movie = get_object_or_404(Movie, pk=movie_pk)
    ratings = movie.rating_set.all()
    form = RatingForm()
    context = {
        'actors':actors,
        'genres':genres,
        'movie_pk':movie_pk,
        'movie':movie,
        'form':form,
        'ratings':ratings
    }
    return render(request, 'page/detail.html', context)