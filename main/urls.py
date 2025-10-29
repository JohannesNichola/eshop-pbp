from django.urls import path
from main.views import (
    show_main, create_products, show_products, 
    show_xml, show_json, show_xml_by_id, show_json_by_id,
    register, login_user, logout_user,
    edit_products, delete_products,
    add_product_ajax, get_products_json,
    edit_product_ajax, delete_product_ajax,
    login_user_ajax, register_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-products/', create_products, name='create_products'),
    path('products/<int:id>/', show_products, name='show_products'),   
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:products_id>/', show_xml_by_id, name='show_xml_by_id'),  
    path('json/<int:products_id>/', show_json_by_id, name='show_json_by_id'),  
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<int:id>/edit/', edit_products, name='edit_products'),  
    path('products/<int:id>/delete/', delete_products, name='delete_products'), 

    # AJAX ROUTES
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('get-products-json/', get_products_json, name='get_products_json'),
    path('edit-product-ajax/<int:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('login-ajax/', login_user_ajax, name='login_user_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
]
