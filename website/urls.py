
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('sobre', views.sobre),
    path('login', views.login),
    path('ideias', views.cadastrar_ideia),
    path('deletar_ideia/<int:id>', views.deletar_ideia)
]