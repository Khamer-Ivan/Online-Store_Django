from django.urls import path

from products.views import (
    CatalogView,
    CategoryView,
    TagView,
    product_detail,
    product_reviews,
    catalog_product,
    all_catalog,
)
from django.conf import settings
from django.conf.urls.static import static

app_name = "products"

urlpatterns = [
    path("catalog/<int:sort>", all_catalog, name="catalog"),
    path("product/<int:pk>/", product_detail, name="product"),
    path("category/<int:pk>/", CategoryView.as_view(), name="category"),
    path("tag/<int:pk>/", TagView.as_view(), name="tag"),
    path("product_reviews/<int:pk>/", product_reviews, name="product_reviews"),
    path("catalog_query/", catalog_product, name="catalog_query"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
