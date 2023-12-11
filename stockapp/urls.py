from django.urls import path
from .views import (
    stock_data_view,
    stock_data_list,
    stock_data_detail,
    stock_data_create,
    stock_data_update,
    stock_data_delete,
    stock_data_viz_view,
)

app_name = 'stockapp'

urlpatterns = [
    path('stock_data1/', stock_data_view, name='stock_data'),
    path('stock_data/list/', stock_data_list, name='stock_data_list'),
    path('stock_data/<int:id>/', stock_data_detail, name='stock_data_detail'),
    path('stock_data/new/', stock_data_create, name='stock_data_create'),
    path('stock_data/<int:id>/edit/', stock_data_update, name='stock_data_update'),
    path('stock_data/<int:id>/delete/', stock_data_delete, name='stock_data_delete'),
    path('data-1/', stock_data_viz_view, name='stock_data_viz'),
]
