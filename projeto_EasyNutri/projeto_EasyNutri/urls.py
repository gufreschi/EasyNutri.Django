from django.urls import path
from app_EasyNutri import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('', views.login, name='login'),
]
