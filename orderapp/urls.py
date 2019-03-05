from django.urls import path, include
from orderapp.views import MenuViewset, OrderViewset


menulist = MenuViewset.as_view({
    'get': 'list',
    'post': 'create',
    'patch': 'partial_update',
    'delete': 'destroy'
})

order_item = OrderViewset.as_view(
    {
        'get' : 'list',
    }
)
"""
menu_detail = MenuViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
"""
urlpatterns = [
    path('menu/', menulist, name='menu-list'),
    #path('menu/<int:pk>', menu_detail, name='menu-detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('order', order_item, name ="order-item")
]