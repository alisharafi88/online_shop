from products.models import Product


class Favorite:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        favorite = self.session.get('favorite')
        if not favorite:
            favorite = self.session['favorite'] = {}
        self.favorite = favorite


    def save(self):
        self.session.modified = True

    def add(self, product):
        product_id = str(product.id)

        if product_id not in self.favorite:
            self.favorite[product_id] = {}
        self.save()


    def __iter__(self):
        favorite_ids = self.favorite.keys()
        products = Product.objects.filter(id__in=favorite_ids)
        favorite = self.favorite.copy()

        for product in products:
            favorite[str(product.id)]['product_obj'] = product
        for item in favorite.values():
            yield item

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.favorite:
            del self.favorite[product_id]
            self.save()

    def clear(self):
        del self.session['favorite']
        self.save()

    def __len__(self):
        return len(self.favorite.keys())
