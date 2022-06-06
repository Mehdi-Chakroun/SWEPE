from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Accueil/', views.request_home, name="accueil"),
    path('Animaux/', views.request_animaux , name="animaux"),
    path('Apropos/', views.request_apropos, name="apropos"),
    path('BD/', views.request_BD, name="BD"),
    path('Contact/', views.request_contact, name="contact"),
    path('Jeu/', views.request_jeu, name="jeu"),
    path('Table_multi/', views.request_Table_multi, name="table"),
    path('Video/', views.request_Video, name="Video"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name= "logout"),
]
