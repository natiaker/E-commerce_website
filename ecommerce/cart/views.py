from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Cart, CartItem
from .models import Product


# view for adding products to the cart
class AddToCartView(LoginRequiredMixin, View):
    login_url = '/login'

    def post(self, request: HttpRequest, product_id):
        redirect_url = request.POST.get('redirect_url')
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        # Check if the product is in stock
        if product.stock > 0:
            # If the product is in the cart
            if cart_item:
                # Check if adding one more quantity exceeds the stock limit
                if cart_item.quantity < product.stock:
                    cart_item.quantity += 1
                    cart_item.save()
                    messages.success(request, f'Added another {product.name} to your cart.')
                else:
                    messages.error(request, 'Stock limit reached.')
            else:
                # If product is not in the cart, create a new cart item
                cart_item = CartItem(cart=cart, product=product, quantity=1)
                cart_item.save()
                messages.success(request, f'Added {product.name} to your cart.')
        else:
            messages.error(request, 'Out of stock')

        if redirect_url:
            return redirect(redirect_url)
        # Redirect to the previous page
        return redirect(request.META.get('HTTP_REFERER'))


# view for removing products from the cart
class RemoveFromCartView(View):
    def post(self, request: HttpRequest, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            if cart_item.quantity > 1:
                # If quantity is more than one, decrement the quantity
                cart_item.quantity -= 1
                cart_item.save()
                messages.success(request, f'One {product.name} removed from your cart.')
            else:
                # If quantity is one, remove the item from the cart
                cart_item.delete()
                messages.success(request, f'{product.name} removed from your cart.')
        else:
            return HttpResponseNotFound("Item not found in the cart.")

        return redirect(request.META.get('HTTP_REFERER'))


