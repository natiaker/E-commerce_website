from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from .models import Product, Category
from .forms import ProductForm




class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        query = request.GET.get('product_query')

        if query:
            products = Product.objects.filter(Q(name__icontains=query))
        else:
            products = Product.objects.all()

        paginator = Paginator(products, 9)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

        return render(request, self.template_name, {'products': products})


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product_details'


class AddProductView(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = '/'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()

        return super().form_valid(form)




