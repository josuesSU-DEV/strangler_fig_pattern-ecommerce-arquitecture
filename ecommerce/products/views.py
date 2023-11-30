from django.shortcuts import render, get_object_or_404
from products.models import Product


def list_products(request):
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "products/list_products.html", context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}
    return render(request, "products/product_detail.html", context)
