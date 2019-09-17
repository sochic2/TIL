from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

app_name="posts"

urlpatterns = [
    path('<int:movie_pk>/ratings/<int:rating_pk>/update/', views.rating_update, name='rating_update'),
    path('<int:movie_pk>/ratings/<int:rating_pk>/delete/', views.delete_rating, name='delete_rating'),
    path('<int:movie_pk>/ratings/new/', views.create_rating, name='create_rating'),
    path('genres/', views.genre_list),
    path('actors/', views.actor_list),
    path('posts/<int:movie_pk>/rating/<int:rating_pk>/', views.rating_update_and_delete),
    path('posts/<int:movie_pk>/rating/', views.rating_create),
    path('posts/<int:movie_pk>/', views.movie_detail),
    path('posts/', views.movie_list), 
    path('docs/', get_swagger_view(title='Api Docs')),
]