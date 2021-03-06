"""AnimeFlix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from AnimeFlix import settings
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_animes),
    path('login/', views.login_user),
    path('login/create_user/', views.create_user),
    path('login/create_user/submit', views.submit_create_user),
    #Indica um POST (com barra indica um GET)
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('add/', views.add_anime),
    path('add/submit', views.submit_add_anime),
    path('delete/', views.delete_anime),
    path('delete/submit', views.submit_delete_anime),
    path('info/', views.info_anime)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
