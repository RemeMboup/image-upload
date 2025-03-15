from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.list_images, name='list_images'),  # Page pour lister les images
    path('upload/', views.upload_image, name='upload'),  # Page pour uploader une image
    path('delete/<int:id>/', views.delete_image, name='delete_image'),  # Supprimer une image
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))), 
]
