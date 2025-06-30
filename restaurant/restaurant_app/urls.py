from django.urls import include, path
from rest_framework import routers
from .views import (
    MenuItemViewSet, TableViewSet, ReservationViewSet,
    InventoryItemViewSet, OrderViewSet, OrderItemViewSet
)

router = routers.DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'inventory', InventoryItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
