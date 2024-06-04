from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('<int:rated_product_id>/delete/<int:id>/', views.delete_rating, name='delete_rating'),
    path('', views.products, name="products"),
]