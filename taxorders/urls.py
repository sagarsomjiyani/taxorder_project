# taxorders/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.tax_order_list, name='tax_order_list'),
    path('contract_details/', views.contract_details_list, name='contract_details_list'),
    path('add_certificate/', views.add_certificate, name='add_certificate'),
    path('enter_consumption/<int:tax_order_id>/', views.enter_consumption, name='enter_consumption'),
    path('tax_order_detail/<int:tax_order_id>/', views.tax_order_detail, name='tax_order_detail'),
    path('add_contract/', views.add_contract, name='add_contract'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Add other URLs as needed
]
