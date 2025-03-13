#Pour generer le formulaire d'inscription

from django import forms
from django.contrib.auth.forms import UserCreationForm

class customUserCreationForm(UserCreationForm):  #classe qui definit les paramettres du mot de passe
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    
    class Meta(UserCreationForm.Meta):  #Personaliser les champs. cette classe permet de drfinir les champs qui doivent s'afficher
        fields = UserCreationForm.Meta.fields + ("password1", "password2")