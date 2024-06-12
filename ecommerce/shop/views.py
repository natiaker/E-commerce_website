from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Product, Category




class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        query = request.GET.get('product_query')

        if query:
            products = Product.objects.filter(Q(title__icontains=query))
        else:
            products = Product.objects.all()

        return render(request, self.template_name, {'products': products})


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product_details'



