from django.db import models
from django.contrib.auth.models import User

RATING = (
    (1, "⭐☆☆☆☆"),
    (2, "⭐⭐☆☆☆"),
    (3, "⭐⭐⭐☆☆"),
    (4, "⭐⭐⭐⭐☆"),
    (5, "⭐⭐⭐⭐⭐"),
    )

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rated_product=models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="ratings")
    author=models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="rating_author")
    rating = models.IntegerField(choices=RATING, default=None, null=True, blank=True) 
    review = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.rated_product} : {self.rating}"


