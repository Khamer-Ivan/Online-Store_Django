from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django import template
from django.db import transaction

from cart.forms import CartAddProductForm
from my_store_app.models import Product, CategoryProduct, TagsFile, Cart, Profile, Reviews
from .forms import ReviewsForm, QueryForm

register = template.Library()


class CatalogView(ListView):
    model = Product
    context_object_name = 'catalog'
    template_name = 'products/catalog.html'


def catalog_product(request: HttpRequest):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['title']
            return render(request, 'products/catalog_query.html', {'query': query})


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


def product_detail(request: HttpRequest, **kwargs):
    if request.method == 'POST':
        product = Product.objects.get(id=kwargs['pk'])
        basket = Cart.objects.filter(username=request.user.profile, product=product)
        with transaction.atomic():
            count = product.count - 1
            Product.objects.filter(id=kwargs['pk']).update(
                count=count
            )

            if not basket.exists():
                Cart.objects.create(
                    username=request.user.profile,
                    product=product,
                    quantity=1
                )
                return redirect('my_store_app:index')

            else:
                cart = basket.first()
                cart.quantity += 1
                cart.save()
                return redirect('my_store_app:index')

    else:
        product = Product.objects.get(id=kwargs['pk'])
        product.reviews += 1
        product.save()
    return render(request, 'products/product.html', {'product': product})


class TagView(DetailView):
    template_name = 'products/tag_page.html'
    model = TagsFile
    context_object_name = 'tags'


def product_reviews(request: HttpRequest, **kwargs):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                Reviews.objects.create(
                    product=Product.objects.get(id=kwargs['pk']),
                    author=Profile.objects.get(user=request.user.id),
                    text=form.cleaned_data['text']
                )
                return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('my_store_app:login')
    else:
        form = ReviewsForm()
        return redirect('products:product')
