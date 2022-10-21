from django.urls import path
from . import views as order_views

urlpatterns = [
    path('cart', order_views.cart, name='cart'),
    path('add_to_cart/<int:food_id>/', order_views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:cart_id>/', order_views.delete_from_cart, name='delete_from_cart'),
    path('order_all/', order_views.order_all, name='order_all'),
    path('order_item/<int:food_id>/', order_views.order_item, name='order_item'),
    path('delete_from_orders/<int:order_id>/', order_views.delete_from_orders, name='delete_from_orders'),
    path('orders/', order_views.orders, name='orders'),
    path('checkout/', order_views.checkout, name='checkout'),
    path('verify-payment/', order_views.verify_payment, name="verify_payment"),
    path('billing_location_form/', order_views.billing_location_form, name='billing_location'),
    path('rating/', order_views.rating, name='rating'),

]

