from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import index, listar_post, post_detalhes

urlpatterns = [
    path('', index, name = 'index'),
    path('lista/', listar_post, name='post_list'),
    path('post-detalhes/<int:pk>/', post_detalhes, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)