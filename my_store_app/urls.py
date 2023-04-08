from django.contrib import admin
from django.urls import include, path
from my_store_app.views import (CategoryView,
                                register_view,
                                AuthorLogoutView,
                                Login,
                                AccountView,
                                ProfileView,
                                HistoryView,
                                CartView,)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

app_name = 'my_store_app'

urlpatterns = [
    path('', CategoryView.as_view(), name='index'),
    path('register/', register_view, name='register'),
    path('logout/', AuthorLogoutView.as_view(), name='logout'),
    path('login/', Login.as_view(template_name='my_store_app/login.html'), name='login'),
    path('email/', views.PasswordResetView.as_view(), name='email'),
    path('account/', AccountView.as_view(), name='account'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('history/', HistoryView.as_view(), name='history'),
    path('cart/', CartView.as_view(), name='cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
