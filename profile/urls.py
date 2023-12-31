from django.contrib import admin
from django.urls import include, path
from profile.views import (
    CategoryView,
    register_view,
    AuthorLogoutView,
    Login,
    AccountView,
    ProfileView,
    CartView,
    avatar,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

# app_name = 'profile'

urlpatterns = [
    path("", CategoryView.as_view(), name="index"),
    path("register/", register_view, name="register"),
    path("logout/", AuthorLogoutView.as_view(), name="logout"),
    path("login/", Login.as_view(template_name="profile/login.html"), name="login"),
    path("email/", views.PasswordResetView.as_view(), name="email"),
    path("account/", AccountView.as_view(), name="account"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("cart/<int:pk>", CartView.as_view(), name="cart"),
    path("avatar/<int:id>", avatar, name="avatar"),
    path("password/", auth_views.PasswordChangeView.as_view(), name="password"),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="profile/password_reset_form.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="profile/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="profile/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="profile/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="profile/password_change_form.html"
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="profile/password_change_done.html"
        ),
        name="password_change_done",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
