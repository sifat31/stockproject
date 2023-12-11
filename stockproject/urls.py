from django.contrib import admin
from django.urls import path, include


from stockapp.views import (
    stock_data_view,
    stock_data_list,
    stock_data_detail,
    stock_data_create,  # Import the stock_data_create view
    stock_data_update,
    stock_data_delete,
    stock_data_viz_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock_data/', stock_data_view, name='stock_data'),
    path('', stock_data_view, name='stock_data_empty'),
    
    path('stock_data_list/', stock_data_list, name='stock_data_list'),
    path('',include('stockapp.urls')),
    path('stock_data_list/', include('stockapp.urls')),

    path('stock_data_detail/<int:id>/', stock_data_detail, name='stock_data_detail'),
    path('stock_data_update/<int:id>/', stock_data_update, name='stock_data_update'),
    path('stock_data_delete/<int:id>/', stock_data_delete, name='stock_data_delete'),
    
    # Add the path for stock_data_create
    path('stock_data_create/', stock_data_create, name='stock_data_create'),
  
    path('stock_data_viz/',stock_data_viz_view , name='stock_data_viz'),
]
