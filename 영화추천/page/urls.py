from django.urls import path
from page import views

app_name="page"

urlpatterns = [
    path('genre/<int:genre_pk>/', views.genre, name='genre'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('list/', views.list, name='list'),
    path('', views.main, name='main'),
    ]