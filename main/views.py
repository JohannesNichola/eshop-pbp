from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()  # ambil semua produk
    context = {
        "app_name": "eshop-pbp",
        "student_name": "Johannes Nichola Simatupang",
        "student_class": "PBP A",
        "products": products}
    return render(request, "main.html", context)
