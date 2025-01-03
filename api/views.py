from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
 )
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Dummy data to display on the home page

posts = [
    {
        'author' : 'Chirag',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'December 27, 2024'
    },
    {
        'author' : 'Rahul',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'December 27, 2024'
    }
]

# Create your views here.
def home(request):
    context = {
        # 'posts': posts  # here we are passing the posts list to the home.html file and this is a dummy data 
        'posts': Post.objects.all() # here we are passing the Post model data to the home.html file
    }
    return render(request, 'api/home.html',context) # here we can pass the context as a dictionary to the home.html file

class PostListView(ListView):
    model = Post
    template_name = 'api/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # here we are ordering the posts in descending order of date_posted
    paginate_by = 5 # here we are paginating the posts by 2 posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'api/user_posts.html' # here we are using the user_posts.html file to display the posts of a particular user
    context_object_name = 'posts'
    ordering = ['-date_posted'] # here we are ordering the posts in descending order of date_posted
    paginate_by = 5 # here we are paginating the posts by 2 posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'api/about.html',{'title': 'About'}) # here we can pass the title as a dictionary to the about.html file