from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def listar_post(request):
    data = {}
    post = Post.objects.filter(data_pub__lte=timezone.now()).order_by('data_pub')
    data['posts'] = post

    return render(request, 'post/list.html', data)

def post_detalhes(request, pk):
    data = {}
    post = get_object_or_404(Post, pk = pk)
    data['post'] = post

    return render(request, 'post/detalhes.html', data)