from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doar/', views.doar, name='doar'),
    path('ursos/', views.ursos, name='ursos'),
    path('urso/<int:urso_id>/', views.detalhes_urso, name='detalhes_urso'),
    path('doacao_sucesso/', views.doacao_sucesso, name='doacao_sucesso'),
]