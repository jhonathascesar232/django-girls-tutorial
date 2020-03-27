from django.urls import path
from .views import index, listar_post

urlpatterns = [
    path('', index, name = 'index'),
    path('lista/', listar_post, name='post_list'),
]
