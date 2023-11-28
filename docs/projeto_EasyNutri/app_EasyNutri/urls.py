from django.urls import path
from app_EasyNutri import views

urlpatterns = [
    path('', views.role, name='role'),
    path('sobre/', views.sobre, name='sobre'),
    ########## PACIENTE ##########
    path('cadastro/', views.register_paciente, name='cadastro-paciente'),
    path('login/', views.login_paciente, name='login-paciente'),
    path('home/', views.home_paciente, name='home-paciente'),
    ########## NUTRICIONISTA ##########
    path('cadastro-nutri/', views.register_nutri, name='cadastro-nutri'),
    path('login-nutri/', views.login_nutri, name='login-nutri'),
    path('home-nutri/', views.home_nutri, name='home-nutri'),
    path('registro/', views.registro, name = 'registro-de-pacientes'),
    path('pacientes/', views.pacientes, name= 'listagem-de-pacientes'),
    ####################
    path('logout/', views.logout_user, name='logout'),
]
