from django.urls import path
from .views import *

urlpatterns = [
    path('', product, name='product_url'),
    path('Product_type/create', Product_typeCreate.as_view(), name='Product_type_create_url'),
    path('Product_type/<int:pk>/update', Product_typeUpdate.as_view(), name='Product_type_update_url'),
    path('Product_type/delete/<int:pk>', Product_typeDelete.as_view(), name='Product_type_delete_url'),
]