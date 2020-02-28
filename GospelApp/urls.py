from django.urls import path
from . import  views 
# app_name = 'GospelApp'



urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.articlepage, name='articlepage'),
    path('books',views.bookpage, name='bookpage'),
    path('books/<int:pk>/', views.book, name='books'),
    path('articles/<int:pk>/', views.articles, name='article'),
    path('videos/<int:pk>/', views.videos, name='video'),
]
