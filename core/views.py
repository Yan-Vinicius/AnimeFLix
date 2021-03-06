from django.shortcuts import render, redirect
from core.models import Anime, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def create_user(request):
    return render(request, 'create_user.html')

def submit_create_user(request):

    if request.POST:

        username = request.POST.get('Username')
        user_email = request.POST.get('Email')
        password = request.POST.get('Password')

        if User.objects.filter(username=username).first():
            messages.error(request, "Usuário já existe")

        else:

            user = User.objects.create_user(username, user_email, password)
            user.save()

            login(request, user)

            return redirect('/')
        return redirect('/')

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

        lista_fav = Profile.objects.get(user=usuario).animes_favoritos.all()

    except Profile.DoesNotExist:

        Profile.objects.create(user=usuario)
        lista_fav = Profile.objects.get(user=usuario).animes_favoritos.all()


    dict_animes = {"animes": todos_animes, "animes_favoritos": lista_fav}
    return render(request, 'index.html', dict_animes)


@login_required(login_url='/login/')
def add_anime(request):

    usuario = request.user
    todos_animes = Anime.objects.all()
    dict_animes = {"animes": todos_animes}


    return render(request, 'add_anime_fav.html', dict_animes)


@login_required(login_url='/login/')
def submit_add_anime(request):

    if request.POST:

        usuario = request.user
        animes_favoritos_usuario = Profile.objects.get(user=usuario)
        lista_animes_selecionados = request.POST.getlist("checks[]")

        for i in lista_animes_selecionados:

            animes = Anime.objects.filter(id=int(i))

            if animes:
                animes_favoritos_usuario.animes_favoritos.add(i)
            else:
                redirect('/')

    return redirect('/')

@login_required(login_url='/login/')
def delete_anime(request):
    usuario = request.user

    try:

        lista_animes_user = Profile.objects.get(user=usuario).animes_favoritos.all()

    except:

        return redirect('/')

    dict_animes = {"animes": lista_animes_user}

    return render(request, 'remover_anime_fav.html', dict_animes)

@login_required(login_url='/login/')
def submit_delete_anime(request):

    usuario = request.user
    lista_animes_selecionados = request.POST.getlist("checks[]")

    for i in lista_animes_selecionados:

        Profile.objects.get(user=usuario).animes_favoritos.remove(int(i))

    return redirect('/')


@login_required(login_url='/login/')
def info_anime(request):

    usuario = request.user

    id_anime = request.GET.get('id')
    dados = {}
    if id_anime:
        dados['anime'] = Anime.objects.get(id=id_anime)

    return render(request,'info_anime.html', dados)