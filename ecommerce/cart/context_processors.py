from .models import CartItem, Cart


def cart_processor(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        cart, cart_created = Cart.objects.get_or_create(user=request.user)
        total_price = cart.total_price()
        total_count = sum(item.quantity for item in cart_items)
    else:
        cart_items = []
        total_price = 0
        total_count = 0

    return {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_count': total_count
    }
