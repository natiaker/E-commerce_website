from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Cart, CartItem
from .models import Product


class AddToCartView(LoginRequiredMixin, View):
    login_url = '/login'

    def post(self, request: HttpRequest, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if product.stock > 0:
            if cart_item:
                if cart_item.quantity < product.stock:
                    cart_item.quantity += 1
                    cart_item.save()
                    messages.success(request, f'Added another {product.name} to your cart.')
                else:
                    messages.error(request, 'Stock limit reached.')
            else:
                cart_item = CartItem(cart=cart, product=product, quantity=1)
                cart_item.save()
                messages.success(request, f'Added {product.name} to your cart.')
        else:
            messages.error(request, 'Out of stock')

        return redirect(request.META.get('HTTP_REFERER'))


class RemoveFromCartView(View):
    def post(self, request: HttpRequest, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, f'One {product.name} removed from your cart.')
            else:
                cart_item.delete()
                messages.success(request, f'{product.name} removed from your cart.')
        else:
            return HttpResponseNotFound("Item not found in the cart.")

        return redirect(request.META.get('HTTP_REFERER'))


