from django.contrib import messages
from django.utils.translation import gettext as _
from django.views import generic

from .models import Product, Comment
from .forms import CommentsForm
from cart.forms import AddToCartForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentsForm()
            context['cart_add']= AddToCartForm()
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            product=self.get_object(),
            user=self.request.user,
            text=self.request.POST.get('text'),
        )
        new_comment.save()
        messages.success(request, _('Yor comment added successfully !'))

        return self.get(self, request, *args, **kwargs)
