from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def listar_post(request):
    data = {}
    return render(request, 'post/list.html', data)