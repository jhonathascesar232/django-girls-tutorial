from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

from .forms import PostForm


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

def novo_post(request):
    data = {}

    if (request.method == 'POST'):
        form = PostForm(request.POST)
        if (form.is_valid()):
            post = form.save(commit = False)
            post.autor = request.user
            post.data_pub = timezone.now()
            post.save()
            return post_detalhes(request, post.pk)
    else:
        form = PostForm()

    data['form'] = form
    return render(request, 'post/form.html', data)

def editar_post(request, pk):
    data = {}

    post = get_object_or_404(Post, pk=pk)

    if (request.method == 'POST'):
        form = PostForm(request.POST, instance = post)

        if (form.is_valid()):
            post = form.save(commit = False)
            post.autor = request.user
            post.data_pub = timezone.now()
            post.save()

            return post_detalhes(request, post.pk)
    else:
        form = PostForm(instance = post)
        data['form'] = form

    return render(request, 'post/form.html', data)
