from django.urls import path
from cart.views import (cart_detail,
                        cart_add,
                        cart_remove,
                        # add_to_cart,
                        delete_product,
                        )

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    # path('add/<int:pk>/', add_to_cart, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('delete/<int:id>', delete_product, name='delete_product')
]
