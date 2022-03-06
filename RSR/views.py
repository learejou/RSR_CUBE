from django.shortcuts import render, get_object_or_404
#from django.http import Http404

from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, id):
    post = get_object_or_404(Post, id=id)
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("Sorry Post not found")
    return render(request, 'blog/show.html', {'id': post})
