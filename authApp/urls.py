from django.urls import path
from .views import *

urlpatterns = [
    path('', inscription, name = 'inscription'),
    path('connexion', connexion, name = 'connexion'),
    path('accueil', accueil, name = 'accueil'),
]
