from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django import template
from django.db import transaction

from my_store_app.models import Product, CategoryProduct, TagsFile, Cart, Profile, Reviews
from .forms import ReviewsForm, QueryForm

register = template.Library()


class CatalogView(ListView):

    """Представление всех товаров в магазине"""

    model = Product
    context_object_name = 'catalog'
    template_name = 'products/catalog.html'


old_sort = 0


def all_catalog(request: HttpRequest, **kwargs):

    """Представление всех товаров в магазине с учётом выбора сортировки"""

    global old_sort

    if request.method == 'GET':
        sort = kwargs['sort']

        if sort == 1:
            catalog = Product.objects.order_by('rating')
            return render(request, 'products/catalog.html', {'catalog': catalog})

        elif sort == 2:
            catalog = Product.objects.order_by('-price')
            return render(request, 'products/catalog.html', {'catalog': catalog})

        elif sort == 3:
            catalog = Product.objects.order_by('reviews')
            return render(request, 'products/catalog.html', {'catalog': catalog})

        elif sort == 4:
            catalog = Product.objects.order_by('date')
            return render(request, 'products/catalog.html', {'catalog': catalog})

        else:
            catalog = Product.objects.all()
            return render(request, 'products/catalog.html', {'catalog': catalog})


def catalog_product(request: HttpRequest):

    """Представление поиска товаров через поисковую строку"""

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['title']
            return render(request, 'products/catalog_query.html', {'query': query})


class CategoryView(DetailView):

    """Представление всех категорий товаров"""

    template_name = 'products/category.html'
    model = CategoryProduct
    context_object_name = 'category'


def product_detail(request: HttpRequest, **kwargs):

    """Детальное представление товара"""

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

    """Представление всех тэгов товаров"""

    template_name = 'products/tag_page.html'
    model = TagsFile
    context_object_name = 'tags'


def product_reviews(request: HttpRequest, **kwargs):

    """Добавление отзывов о товаре"""

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
