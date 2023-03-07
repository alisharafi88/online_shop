from django.urls import path

from .views import cart_detail_view, add_to_cart_view, remove_product_view, clear_cart_view

urlpatterns = [
    path('', cart_detail_view, name='cart_details'),
    path('add/<int:product_id>/', add_to_cart_view, name='cart_add'),
    path('remove/<int:product_id>/', remove_product_view, name='cart_remove'),
    path('clear/', clear_cart_view, name='cart_clear'),
]
