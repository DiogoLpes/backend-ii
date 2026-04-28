from django.urls import path
from . import views

urlpatterns = [
    # HTML Pages
    path("", views.home, name="home"),
    path("cart/", views.cart_page, name="cart_page"),
    
    # API Products
    path("api/products/", views.product_list, name="product_list"),
    path("api/products/<int:product_id>/", views.product_detail, name="product_detail"),
    
    # API Cart
    path("api/cart/", views.cart_view, name="cart_view"),
    path("api/cart/add/<int:product_id>/", views.add_to_cart_simple, name="add_to_cart_simple"),
    path("api/cart/remove/<int:product_id>/", views.remove_from_cart_simple, name="remove_from_cart_simple"),
    path("api/cart/pay/", views.pay_cart, name="pay_cart"),
    
    # Legacy Order endpoints
    path("api/orders/", views.order_list, name="order_list"),
    path("api/orders/<int:order_id>/", views.order_detail, name="order_detail"),
    path("api/orders/<int:order_id>/pay/", views.pay_order, name="pay_order"),
]