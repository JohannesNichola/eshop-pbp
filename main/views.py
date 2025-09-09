from django.shortcuts import render
from .models import Product

def show_main(request):
    products = Product.objects.all()  # ambil semua produk
    context = {"products": products}
    return render(request, "main.html", context)
