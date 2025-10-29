from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products_list = Products.objects.all()
    else:
        products_list = Products.objects.filter(user=request.user)

    context = {
        'app': 'Offside!',
        'name': request.user.username,
        'npm' : '2406495930',
        'class': 'PBP A',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'show_navbar': True,  # tampilkan navbar di halaman ini
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        products_entry = form.save(commit=False)
        products_entry.user = request.user
        products_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'show_navbar': True,  # tampilkan navbar di halaman ini
    }

    return render(request, "create_products.html", context)

@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Products.objects.all()
    data = []

    for product in products_list:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "thumbnail": product.thumbnail,
            "category": product.category,
            "is_featured": product.is_featured,
            "products_views": product.products_views,
            "user_id": product.user.id if product.user else None,
            "user_username": product.user.username if product.user else None,
        })

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, products_id):
    try:
        products_item = Products.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)
   
def show_json_by_id(request, products_id):
    try:
        products = Products.objects.select_related('user').get(pk=products_id)
        data = {
            'id': str(products.id),
            'name': products.name,
            'price': products.price,
            'description': products.description,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'products_views': products.products_views,
            'is_featured': products.is_featured,
            'user_id': products.user_id,
            'user_username': products.user.username if products.user_id else None,
        }
        return JsonResponse(data)
    except Products.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
        
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
        
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_products(request, id):
    products = get_object_or_404(Products, pk=id)
    form = ProductsForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_products.html", context)

def delete_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # handle checkbox
    user = request.user if request.user.is_authenticated else None

    new_product = Products(
        user=user,
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
    )
    new_product.save()

    return JsonResponse({"status": "success", "message": "Product created successfully!"}, status=201)


@login_required(login_url='/login')
def get_products_json(request):
    products = Products.objects.filter(user=request.user)
    data = serializers.serialize("json", products)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def edit_product_ajax(request, id):
    product = get_object_or_404(Products, pk=id, user=request.user)
    product.name = strip_tags(request.POST.get("name"))
    product.price = strip_tags(request.POST.get("price"))
    product.description = request.POST.get("description")
    product.category = request.POST.get("category")
    product.thumbnail = request.POST.get("thumbnail")
    product.is_featured = request.POST.get("is_featured") == 'on'
    product.save()
    return JsonResponse({"status": "updated"})

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    product = get_object_or_404(Products, pk=id, user=request.user)
    product.delete()
    return JsonResponse({"status": "deleted"})

@csrf_exempt
@require_POST
def login_user_ajax(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        response = JsonResponse({"status": "success"})
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        return JsonResponse({"status": "error", "message": "Invalid credentials"}, status=401)

@csrf_exempt
def register_ajax(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": "success",
                "message": "Your account has been successfully created!"
            }, status=201)
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid form input.",
                "errors": form.errors
            }, status=400)
    else:
        return JsonResponse({
            "status": "error",
            "message": "Invalid request method."
        }, status=405)