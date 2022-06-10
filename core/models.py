from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Anime(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_lancamento = models.DateField(verbose_name="Data de Lançamento")
    num_episodios = models.IntegerField()
    imagem = models.ImageField(upload_to='media')


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    animes_favoritos = models.ManyToManyField(Anime, blank=True)

