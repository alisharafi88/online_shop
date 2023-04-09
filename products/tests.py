from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import TestCase

from .models import Product
from .views import ProductListView


class TestProduct(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a sample image file
        image_content = b'binary content of the image'
        image_file = SimpleUploadedFile('test_image.jpg', image_content, content_type='image/jpeg')

        for i in range(10):
            Product.objects.create(
                title=f'Product {i}',
                description=f'Product description {i}',
                price=10*i,
                active=True,
                cover=image_file
            )

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('products_list'))
        self.assertTemplateUsed(response, 'products/product_list.html')
