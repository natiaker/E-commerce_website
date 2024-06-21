from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, View, DeleteView, UpdateView, ListView, RedirectView
from .models import Product
from .forms import ProductForm, RegistrationForm
from order.models import OrderItem, Order


# view for the homepage with product list and search functionality
class IndexView(TemplateView):
    template_name = 'index.html'

    # filter products based on search query or category
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        query = request.GET.get('product_query')
        category_query = request.GET.get('category')

        if query:
            products = Product.objects.filter(Q(name__icontains=query)).order_by('name')
        elif category_query:
            products = Product.objects.filter(categories__id=category_query).order_by('name')
        else:
            products = Product.objects.all().order_by('name')

        # paginate the product list
        paginator = Paginator(products, 9)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

        return render(request, self.template_name, {'products': products, 'category_query': category_query, 'product_query': query or ''})


# view for displaying product details
class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product_details'


# view for adding a new product, requires appropriate permissions
class AddProductView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = '/'
    permission_required = 'shop.add_product'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()

        return super().form_valid(form)

    def handle_no_permission(self):
        return redirect('shop:homepage')


# view for removing a product, requires appropriate permissions
class RemoveProductView(PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('shop:homepage')
    template_name = 'confirm_delete.html'
    permission_required = 'shop.delete_product'

    def handle_no_permission(self):
        return redirect('shop:homepage')


# view for editing a product, requires appropriate permissions
class EditProductView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'categories', 'stock', 'image']
    template_name = 'update_product.html'
    success_url = '/'
    permission_required = 'shop.change_product'

    def handle_no_permission(self):
        return redirect('shop:homepage')


# View for user registration
class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'
    success_url = '/login'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()

        return super().form_valid(form)


# view for user login, only accessible to non-authenticated users
class UserLoginView(UserPassesTestMixin, LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('shop:homepage')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('shop:homepage')


# View for user logout
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('shop:login')


# View for displaying user profile with order history, requires login
class UserProfileView(LoginRequiredMixin, ListView):
    template_name = 'user_profile.html'
    context_object_name = 'orders'
    login_url = '/login'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-order_date")

