from django.urls import path
from . import views
app_name = 'Order_System'
urlpatterns = [
    path('', views.OrderCreateView.as_view() , name = 'Odrer'),
    path('finish/', views.FinishView.as_view() , name = 'finish'),
    path('orderlist/', views.OrderListView.as_view(), name = 'order_list'),
    path('detail/<str:pk>', views.OrderDetailView.as_view(), name = 'orderdetail'),
    path('Update/<str:pk>', views.OrderUpdateView.as_view(), name = 'OrderUpdate'),
    path('Delete/<str:pk>', views.OrderDeleteView.as_view(), name = 'OrderDelete')
]