from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # /
    path('products/', views.product_list),        # /products/
    path('products/<int:id>/', views.product_detail), # /products/1/
]
