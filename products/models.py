from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.ForeignKey('Rating', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rating = models.CharField(max_length=100, null=True)


