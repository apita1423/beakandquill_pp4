from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

# Code Credit: CI I Think Therefore I Blog Walkthrough
class PostList(generic.ListView):
    model = Post