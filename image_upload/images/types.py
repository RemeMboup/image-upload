import graphene
from .models import Image

class ImageType(graphene.ObjectType):
    id = graphene.Int()
    image = graphene.String()

    # Définissez d'autres champs que vous souhaitez exposer via GraphQL
    def resolve_image(self, info):
        return self.image.url  # Retourne l'URL de l'image stockée
