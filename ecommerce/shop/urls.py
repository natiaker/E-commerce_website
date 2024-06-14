
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('product_details/<int:pk>', views.ProductDetailsView.as_view(), name='product_details'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
