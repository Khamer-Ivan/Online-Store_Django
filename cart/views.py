from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from my_store_app.models import Product, Cart
from .cart import Cart as Basket
from .forms import CartAddProductForm
from django.views.generic import ListView, DetailView, DeleteView


@require_POST
def cart_add(request, product_id):
    cart = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        # cart.save()
    print('=' * 70)
    for i in cart:
        print('+' * 25)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request: HttpRequest, **kwargs):
    cart = Cart.objects.filter(username=kwargs['pk'])
    return redirect('my_store_app:cart')


# def add_to_cart(request: HttpRequest, **kwargs):
# if request.method == 'POST':
#     product = Product.objects.get(id=kwargs['pk'])
#     print(f'PRODUCT: {product.title}, {product.price}')
#     basket = Basket.objects.filter(username=request.user.username, product=product)
#
#     if not basket.exists():
#         Basket.objects.create(
#             username=request.user.username,
#             product=product,
#             quantity=1
#         )
#         return redirect('my_store_app:index')
#
#     else:
#         cart = basket.first()
#         cart.quantity += 1
#         cart.save()
#         return redirect('my_store_app:index')
# else:
#     product = Product.objects.get(id=kwargs['pk'])
# return render(request, 'products/product.html', {'product': product})


def delete_product(request: HttpRequest, **kwargs):
    Cart.objects.get(id=kwargs['id']).delete()
    return redirect(request.META['HTTP_REFERER'])


