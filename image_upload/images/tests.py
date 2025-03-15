from django.test import TestCase
from django.urls import reverse
from .models import Image

class ImageUploadTests(TestCase):

    def test_image_upload(self):
        # Simulate uploading an image
       with open('C:\\Users\\pc\\Pictures\\Image\\Mareme.png', 'rb') as image_file:
            response = self.client.post(reverse('upload'), {
                'image': image_file,
            })
            self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_image_gallery(self):
        # Simulate viewing the gallery
        Image.objects.create(image='C:\\Users\\pc\\Pictures\\Image\\Mareme.png')
        response = self.client.get(reverse('list_images'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Uploaded Images')
