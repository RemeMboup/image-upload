import graphene
from .mutations import CreateImage  # Importez votre mutation
from .types import ImageType  # Assurez-vous que ImageType est importé
from .models import Image
class Mutation(graphene.ObjectType):
    create_image = CreateImage.Field()  # Ajoutez la mutation ici

class Query(graphene.ObjectType):
    # Exemple de query pour lister les images
    all_images = graphene.List(ImageType)

    def resolve_all_images(self, info):
        return Image.objects.all()  # Retourne toutes les images

schema = graphene.Schema(query=Query, mutation=Mutation)
