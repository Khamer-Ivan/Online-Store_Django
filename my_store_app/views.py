from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from my_store_app.models import (Profile,
                                 Sales,
                                 CategoryProduct,
                                 Product, TagsFile,
                                 Reviews,
                                 Specifications,
                                 OrderHistory,
                                 Order,
                                 Basket,
                                 Payment,
                                 Shop
                                 )
from my_store_app.forms import AuthorRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User
import os
from django.core.exceptions import ValidationError


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

    return render(request, 'my_store_app/registr.html')


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
        print(file_name_list)
        category = zip(date, file_name_list)
        popular_product = Product.objects.all().order_by('-reviews')[:8]
        limited_edition = Product.objects.filter(free_delivery=False)
        banners = Product.objects.all().order_by('-rating')
        return render(request, 'my_store_app/index.html', {'popular_product': popular_product,
                                              'limited_edition': limited_edition,
                                              'banners': banners})


class AccountView(View):
    def get(self, request: HttpRequest):
        return render(request, 'my_store_app/account.html')


class ProfileView(View):
    def get(self, request: HttpRequest):
        return render(request, 'my_store_app/profile.html')


class HistoryView(View):
    def get(self, request: HttpRequest):
        return render(request, 'my_store_app/historyorder.html')