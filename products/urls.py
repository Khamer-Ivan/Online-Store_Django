from django.urls import path

from products.views import CatalogView, ProductView, CategoryView, ProductDetail, TagView, product_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product//<int:pk>/', product_detail, name='product'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
