from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']  # Liste des champs que tu veux dans le formulaire
