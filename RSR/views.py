from django.shortcuts import render

from .mocks import Post


# Create your views here.
def index(request):
    posts = Post.all
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, id):
    post = Post.find(id)
    return render(request, 'blog/show.html', {'id': post})
