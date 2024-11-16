from django.urls import path
from . import views

urlpatterns=[
    path('',views.product_list, name='product_list'),
    path('<int:primaryKey>/',views.product_detail, name='product_detail'),
    path('new/', views.product_create, name='product_create'),
    path('listview',views.ProductoListView.as_view(), name ='product_listview'),
    path('detailview/<int:pk>/',views.ProductoDetailView.as_view(), name ='product_detailview'),
    path('updateview/<int:pk>/',views.ProductoUpdateView.as_view(), name ='product_updateview'),
    path('createview/',views.ProductoCreateView.as_view(), name ='product_createview'),
    path('deleteview/<int:pk>/',views.ProductoDeleteView.as_view(), name ='product_deleteview')
    ,path('delete/<int:pk>/',views.producto_delete, name ='product_delete'),
    path('proveedor/<int:proveedor_id>/',views.proveedor_detail,name ='proveedor_detail')
]