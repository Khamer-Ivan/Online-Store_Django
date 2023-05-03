from django.urls import path
from cart.views import (cart_detail,
                        # add_to_cart,
                        delete_product,
                        update_product,
                        )

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('update/<int:id>', update_product, name='update_product'),
]
