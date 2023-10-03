from . import views
from django.urls import path

urlpatterns = [
    path('',views.file,name='file'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('showprod',views.showprod,name='showprod'),
    path('prod_edit/<int:px>/',views.prod_edit,name='prod_edit'),
    path('edit/<int:px>/', views.edit, name='edit'),
    path('delete/<int:px>/',views.delete,name='delete'),
]
