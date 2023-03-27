from django.urls import path

from .views import favorite_detail_view, add_favorite_view, remove_favorite_view
urlpatterns = [
    path('', favorite_detail_view, name='favorite'),
    path('add/<int:product_id>/', add_favorite_view, name='add_favorite'),
    path('remove/<int:product_id>/', remove_favorite_view, name='remove_favorite')
]
