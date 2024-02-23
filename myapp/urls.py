from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('products/', views.product_list, name='product_list'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]