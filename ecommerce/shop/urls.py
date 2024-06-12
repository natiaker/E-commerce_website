
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('product_details/<int:pk>', views.ProductDetailsView.as_view(), name='product_details'),
]
