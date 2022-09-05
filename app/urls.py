from app.models import Products
from .views import Feedback_API, Profile_API, RegisterAPI, LoginAPI, UserAPI, Products_API, Product_API, Products_by_category1_API, Products_by_category2_API, Cart_API, Orders_API
from knox import views as knox_views
from django.urls import path


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),

    path('api/profile/', Profile_API.as_view(), name='user-profile'),
    path('api/products/', Products_API.as_view(), name='products'),
    path('api/product/<int:pk>/', Product_API.as_view(), name='product'),
    path('api/products/<category_one>/',
         Products_by_category1_API.as_view(), name='category_one'),
    path('api/products/<category_two>/',
         Products_by_category2_API.as_view(), name='category_one'),
    path('api/cart/', Cart_API.as_view(), name='user-cart'),
    path('api/orders/', Orders_API.as_view(), name='user-orders'),
    path('api/feedback/', Feedback_API.as_view(), name='user-feedback'),

    path('api/update/orders/<int:pk>/',
         Orders_API.as_view(), name='update_user-orders'),
]
