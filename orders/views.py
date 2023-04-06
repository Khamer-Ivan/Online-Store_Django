from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class OrderView(View):
    def get(self, request: HttpRequest):
        return render(request, 'orders/order.html')
