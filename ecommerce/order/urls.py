from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('', views.OrderPageView.as_view(), name='order_page'),
]


