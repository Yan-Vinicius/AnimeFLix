from django.shortcuts import render, redirect
from core.models import Anime, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')

        else:
            messages.error(request, message="Usuário ou senha inválido")

    return redirect('/')



def logout_user(request):
    logout(request)

    return redirect('/')


@login_required(login_url="/login/")
def lista_animes(request):

    usuario = request.user
    todos_animes = Anime.objects.all()

    try:

        lista_fav = Profile.objects.get(id=usuario.id).animes_favoritos.all()

    except Profile.DoesNotExist:

        Profile.objects.create(user=usuario)

        lista_fav = Profile.objects.get(id=usuario.id).animes_favoritos.all()


    dict_animes = {"animes": todos_animes, "animes_favoritos": lista_fav}
    return render(request, 'index.html', dict_animes)


def create_user(request):
    return