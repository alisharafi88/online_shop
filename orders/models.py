from django.db import models
from django.utils.translation import gettext as _

from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is Paid?'), default=False)

    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=150)
    phone_number = PhoneNumberField(null=False, blank=False, verbose_name=_('Phone Number'))
    address = models.CharField(_('Address'), max_length=1000)
    order_nots = models.CharField(_('Note'), max_length=500)

    datetime_created = models.DateTimeField(_('Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.item.all())

    # def get_total_price(self):
    #     return sum(item.quantity * item.price for item in self.items.all())


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item', verbose_name=_('Item'))
    product = models.ForeignKey('products.Product',
                                on_delete=models.CASCADE,
                                related_name=_('order_product'),
                                verbose_name='Product')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} x {self.quantity} (price:{self.price})'
