from django.urls import path, include

from .views import (
    # FBV
    home,
    # CBV
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
)

urlpatterns = [
    path('list/', OrderListView.as_view(), name='order_list'),
    path('detail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),
    path('', home, name='home'),
]