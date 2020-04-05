from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_pub = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_pub = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo