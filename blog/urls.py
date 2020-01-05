from django.urls import path
from blog import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='blog-home'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/<int:pk>/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('movie/<int:pk>/review/', views.ReviewCreateView.as_view(), name='review-create'),
    path('upvote/<int:movie_id>/', views.upvote, name='upvote'),
    path('downvote/<int:movie_id>/', views.downvote, name='downvote'),
    path('about/', views.about, name='blog-about'),
    path('toprated/', views.toprated, name='blog-toprated')
]
