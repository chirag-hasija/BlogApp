from django.contrib import admin
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('', views.home,name='api-home'),
    path('post/', PostListView.as_view(),name='api-post'),
    path('user/<str:username>/', UserPostListView.as_view(),name='api-user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='api-post-detail'),
    path('post/new/', PostCreateView.as_view(),name='api-post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='api-post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='api-post-delete'),
    path('about/', views.about,name='api-about'), 
]