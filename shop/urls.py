from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('order/confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order/confirmation/<int:pk>/', views.order_confirmation, name='order_confirmation'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),

]

