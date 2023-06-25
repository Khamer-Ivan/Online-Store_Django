from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView

from profile.models import Profile
from products.models import Product, TagsFile, Reviews, Specifications, Shop, Sales, CategoryProduct
from orders.models import Order, OrderHistory
from cart.models import Cart, Payment

from profile.forms import AuthorRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User
import os
from django.core.exceptions import ValidationError
from cart.forms import CartAddProductForm


def register_view(request):
    """Функция регистрации нового пользователя"""

    if request.method == 'POST':
        form = AuthorRegisterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('login')
            user = User.objects.create_user(username=username, first_name=full_name, email=email)
            user.set_password(raw_password)
            user.save()
            login(request, user)
            Profile.objects.create(user=user, username=username, full_name=full_name, phone=phone, email=email)
        return redirect('/')

    return render(request, 'profile/registr.html')


class AuthorLogoutView(LogoutView):
    """Выход из учетной записи"""

    next_page = '/'


class Login(LoginView):
    """Вход в учетную запись"""

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryView(View):
    """Формирование списка категорий, популярных товаров,
     лимитированных, баннеров и путей до изображений этих категорий"""

    def get(self, request):
        date = CategoryProduct.objects.all()
        file_name_list = []
        for image in date:
            file = os.path.basename(str(image.image))
            file_name_list.append(file)
        category = zip(date, file_name_list)
        popular_product = Product.objects.all().order_by('-reviews')[:8]
        limited_edition = Product.objects.filter(free_delivery=False)
        banners = Product.objects.all().order_by('-rating')
        return render(request, 'profile/index.html', {'popular_product': popular_product,
                                                           'limited_edition': limited_edition,
                                                           'banners': banners})


class AccountView(View):
    def get(self, request: HttpRequest):
        return render(request, 'profile/account.html')


class ProfileView(View):
    def get(self, request: HttpRequest):
        return render(request, 'profile/profile.html')


class CartView(View):
    def get(self, request: HttpRequest, **kwargs):
        cart = Cart.objects.filter(username=kwargs['pk'])
        total_price = 0
        for product in cart:
            total_price += product.product.price * product.quantity
        return render(request, 'cart/cart.html', {'total_price': total_price})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product.html', {'product': product,
                                                     'cart_product_form': cart_product_form})


def avatar(request: HttpRequest, **kwargs):
    user = Profile.objects.get(user=kwargs['id'])
    user_avatar = request.POST.get('avatar')

    Profile.objects.filter(user=kwargs['id']).update(
        avatar=user_avatar,
    )
    return redirect(request.META['HTTP_REFERER'])
