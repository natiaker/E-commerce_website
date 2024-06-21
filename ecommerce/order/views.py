from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from order.forms import OrderForm
from cart.models import Cart, CartItem
from order.models import Order, CustomerInfo, OrderItem


class OrderPageView(LoginRequiredMixin, CreateView):
    template_name = 'order_page.html'
    form_class = OrderForm
    login_url = '/login'
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)
        customer_info = self.object

        cart = get_object_or_404(Cart, user=self.request.user)

        order = Order.objects.create(
            user=self.request.user,
            customer_info=customer_info
        )

        cart_items = CartItem.objects.filter(cart=cart).all()

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        cart.delete()

        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        context['cart_items'] = cart_items
        return context

