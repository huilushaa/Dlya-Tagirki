from django.urls import path

from orders.views import (CancelTemplateView, OrderCreateView, OrderDetailView,
                          OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order-success'),
    path('order-canceled/', CancelTemplateView.as_view(), name='order-canceled'),
    path('', OrderListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
]
