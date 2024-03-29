from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# Code Credit: CI I Think Therefore I Blog Walkthrough
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # Orders the Post from newest to oldest
    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    

# Code Credit: CI I Think Therefore I Blog Walkthrough
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField() 
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # Orders the Comments from oldest to newest
    class Meta: ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    