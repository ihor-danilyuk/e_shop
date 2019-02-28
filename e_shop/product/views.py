from django.shortcuts import render
from .models import Category, Product
from django.http import HttpResponse


# Create your views here.
def index(request):
    ctx = {}
    ctx['all_categories'] = Category.objects.all()
    return render(request, 'index.html', ctx)


def show_product(request):
    ctx = {}
    ctx['all_product'] = Product.objects.all()
    return render(request, 'product/product.html', ctx)