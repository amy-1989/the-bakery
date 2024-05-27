from django.urls import path
from . import views

urlpatterns = [
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('address', views.address, name='profile_address'),
    path('address/set_primary/<slug:id>', views.set_primary_address, name='set_primary_address'),
    path('', views.profile, name='profile'),
]