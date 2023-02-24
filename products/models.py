from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='covers')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}:{self.price}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(models.Model):
    POINT_CHOICES = [
        ("1", 'very bad'),
        ("2", 'bad'),
        ("3", 'normal'),
        ("4", 'good'),
        ("5", 'very good'),

    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    text = models.TextField(verbose_name="متن")
    point = models.CharField(max_length=10, choices=POINT_CHOICES)
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
