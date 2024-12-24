from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.list_orders, name='list_orders'),
    path('create_order/',views.create_order,name="create_order"),
    path('update_order/',views.update_order,name='update_order')
]
