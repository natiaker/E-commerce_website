from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView
from order.forms import OrderForm
from cart.models import Cart, CartItem
from order.models import Order, CustomerInfo, OrderItem


class OrderPageView(LoginRequiredMixin, CreateView):
    template_name = 'order_page.html'
    form_class = OrderForm
    login_url = '/login'
    success_url = '/user_profile'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        res = super().form_valid(form)
        customer_info = self.object

        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart).all()

        # Check if cart is empty
        if cart_items:
            order = Order.objects.create(
                user=self.request.user,
                customer_info=customer_info
            )
        else:
            messages.error(self.request, 'Cart is empty.')
            return redirect(self.request.META.get('HTTP_REFERER'))

        # Create the order and related order items
        try:
            with transaction.atomic():
                for item in cart_items:
                    product = item.product
                    OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                    product.stock -= item.quantity
                    product.save()

                cart.delete()

                messages.success(self.request, 'Your order has been placed successfully!')

        except Exception as e:
            messages.error(self.request, f'Failed to place the order: {str(e)}')

        return res

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = get_object_or_404(Cart, user=self.request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        context['cart_items'] = cart_items
        return context

