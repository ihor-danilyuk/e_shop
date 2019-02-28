from django.shortcuts import render
from .models import Category

# Create your views here.
def index(request):
    ctx = {}
    ctx['all_categories'] = Category.objects.all()
    return render(request, 'index.html', ctx)