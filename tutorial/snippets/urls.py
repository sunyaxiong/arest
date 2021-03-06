from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
    path('inventory', views.inventory_list),
    path('inventory/<int:pk>', views.inventory_detail),

    path('orders', views.order_list),
    path('users', views.user_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
