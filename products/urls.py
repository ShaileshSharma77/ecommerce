from django.urls import path
from . import views
#from django.views.generic import TemplateView


urlpatterns =[
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('/add', views.add_product, name='add_product'),
    path('update/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),

]