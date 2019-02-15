from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
    path('qna/', views.qna, name='qna'),
    path('', views.index, name='index'),
    path('<str:a>/', views.not_found, name='not_found'),
]