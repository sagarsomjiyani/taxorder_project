# taxorders/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.tax_order_list, name='tax_order_list'),
    path('add_certificate/', views.add_certificate, name='add_certificate'),
    path('enter_consumption/<int:tax_order_id>/', views.enter_consumption, name='enter_consumption'),
    path('tax_order_detail/<int:tax_order_id>/', views.tax_order_detail, name='tax_order_detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Add other URLs as needed
]
