from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm  # Si tu utilises un formulaire pour l'upload

# Vue pour lister les images
def list_images(request):
    # Récupère toutes les images dans la base de données
    images = Image.objects.all()
    # Rends la page list.html avec les images
    return render(request, 'images/list.html', {'images': images})

# Vue pour uploader une nouvelle image
def upload_image(request):
    # Si la méthode de requête est POST, cela signifie qu'un formulaire a été soumis
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Si le formulaire est valide, sauvegarde l'image et redirige vers la page de liste
            form.save()
            return redirect('list_images')  # Redirige vers la liste des images après l'upload
    else:
        # Si ce n'est pas une requête POST, on crée un formulaire vide
        form = ImageForm()

    # Rends la page upload.html avec le formulaire pour uploader une image
    return render(request, 'images/upload.html', {'form': form})

# Vue pour supprimer une image
def delete_image(request, id):
    # Récupère l'image par son ID
    image = Image.objects.get(id=id)
    # Supprime l'image
    image.delete()
    # Redirige vers la liste des images après la suppression
    return redirect('list_images')
