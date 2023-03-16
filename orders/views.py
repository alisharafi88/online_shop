from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required


from cart.cart import Cart
from .forms import CheckoutForms
from .models import ItemOrder


@login_required
def order_create_view(request):
    order_form = CheckoutForms()
    cart =Cart(request)
    if len(cart) == 0:
        messages.warning(request, _('You can not proceed to checkout page because your cart is empty.'))
        return redirect('products_list')

    if request.method == 'POST':
        order_form = CheckoutForms(request.POST)
        if order_form.is_valid():
            order_obj=order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                ItemOrder.objects.create(
                    order=order_obj,
                    product=item['product_obj'],
                    quantity=item['quantity'],
                    price=item['product_obj'].price,
                )
            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()


    return render(request, 'orders/checkout.html',  {
        'form': order_form})
