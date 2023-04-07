from django.shortcuts import render, get_object_or_404, redirect

from . favorite import Favorite
from products.models import Product


def favorite_detail_view(request):
    favorite = Favorite(request)
    return render(request, 'favorite/favorite.html', {'favorite': favorite})


def add_favorite_view(request, product_id):
    favorite = Favorite(request)
    product = get_object_or_404(Product, id=product_id)
    favorite.add(product)

    return redirect('favorite')


def remove_favorite_view(request, product_id):
    favorite = Favorite(request)
    product = get_object_or_404(Product, id=product_id)
    favorite.remove(product)
    if len(favorite):
        return redirect('favorite')
    return redirect('products_list')
