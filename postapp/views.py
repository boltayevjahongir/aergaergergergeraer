from django.shortcuts import render
from .models import Post
# Create your views here.
def blog(req):
    posts = Post.objects.all()[:6]
    return render(req, 'blog.html',
                  context={
                      'posts':posts
                  })