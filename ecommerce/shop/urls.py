from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('product_details/<int:pk>', views.ProductDetailsView.as_view(), name='product_details'),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('remove_product/<int:pk>', views.RemoveProductView.as_view(), name='remove_product'),
    path('edit_product/<int:pk>', views.EditProductView.as_view(), name='edit_product'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user_profile/', views.UserProfileView.as_view(), name='user_profile')
]


