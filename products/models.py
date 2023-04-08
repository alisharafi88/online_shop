from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    short_description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='covers', blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}:{self.price}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(models.Model):
    POINT_CHOICES = [
        ("1", _('very bad')),
        ("2", _('bad')),
        ("3", _('normal')),
        ("4", _('good')),
        ("5", _('very good')),

    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    text = models.TextField(verbose_name=_("text"))
    point = models.CharField(max_length=10, choices=POINT_CHOICES, verbose_name=_('point'))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
