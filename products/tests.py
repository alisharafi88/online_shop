from django.test import TestCase, SimpleTestCase

from django.urls import reverse
from django.test import TestCase
from .models import Product
from .views import ProductListView


class TestProduct(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(10):
            Product.objects.create(
                title = f'Product {i}',
                description= f'Product description {i}',
                price = 10*i,
                active = True,
            )

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('products_list'))
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_view_pagination_is_four(self):
        request = self.client.get(reverse('products_list'))
        product_list_view = ProductListView.as_view()
        response = product_list_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context_data['products']), 4)

    def test_queryset_returns_only_active_products(self):
        request = self.client.get(reverse('products_list'))
        product_list_view = ProductListView.as_view()
        response = product_list_view(request)
        self.assertEqual(response.status_code, 200)
        for product in response.context_data['products']:
            self.assertEqual(product.active, True)
