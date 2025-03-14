from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import customUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def inscription(request):                               #definition de la vue de la page inscription
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
        return redirect('accueil')
    else:
        form = customUserCreationForm()
    return render(request, 'inscription.html', {'form' : form})

def connexion(request):                              #definition de la vue de la page connexion
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else :
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

def accueil(request):                            #definition de la vue de la page accueil
    return render(request, "accueil.html")