from django.contrib import admin
from django.urls import path
from django.urls import include, path
from my_store_app.views import Profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include("my_store_app.urls")),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('password/', auth_views.PasswordChangeView.as_view(), name='password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='my_store_app/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='my_store_app/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='my_store_app/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='my_store_app/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='my_store_app/password_change_form.html'),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='my_store_app/password_change_done.html'),
         name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
