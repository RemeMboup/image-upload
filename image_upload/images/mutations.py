import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload  # Ceci est nécessaire pour gérer les fichiers
from .models import Image

class ImageType(DjangoObjectType):
    class Meta:
        model = Image

class CreateImage(graphene.Mutation):
    image = graphene.Field(ImageType)

    class Arguments:
        image = Upload(required=True)  # Utilisez `Upload` pour accepter un fichier

    def mutate(self, info, image):
        # Sauvegarde de l'image (vous pouvez gérer la logique pour sauvegarder le fichier)
        new_image = Image.objects.create(image=image)
        return CreateImage(image=new_image)
