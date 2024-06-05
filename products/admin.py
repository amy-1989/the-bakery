from django.contrib import admin
from .models import Product, Category, Rating, Comment


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Comment)