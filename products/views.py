from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django import template

from my_store_app.models import Product, CategoryProduct, TagsFile

register = template.Library()


class CatalogView(ListView):
    model = Product
    context_object_name = 'catalog'
    template_name = 'products/catalog.html'


class CategoryView(DetailView):
    template_name = 'products/category.html'
    model = CategoryProduct
    context_object_name = 'category'


class ProductView(View):
    def get(self, request: HttpRequest):
        return render(request, 'products/product.html')


class ProductDetail(DetailView):
    template_name = 'products/product.html'
    model = Product
    context_object_name = 'product'


class TagView(DetailView):
    template_name = 'products/tag_page.html'
    model = TagsFile
    context_object_name = 'tags'
