from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MenuItem, Table, Reservation, InventoryItem, Order, OrderItem
from .serializers import (
    MenuItemSerializer, TableSerializer, ReservationSerializer,
    InventoryItemSerializer, OrderSerializer, OrderItemSerializer
)

# Menu
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Tables
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

# Réservations avec vérification de la table
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        table_id = request.data.get('table')
        try:
            table = Table.objects.get(id=table_id)

            if not table.is_available:
                return Response({'error': 'Table non disponible'}, status=status.HTTP_400_BAD_REQUEST)

            table.is_available = False
            table.save()

            return super().create(request, *args, **kwargs)

        except Table.DoesNotExist:
            return Response({'error': 'Table introuvable'}, status=status.HTTP_404_NOT_FOUND)

# Inventaire
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

# Commandes avec traitement
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'])
    def process_order(self, request, pk=None):
        order = self.get_object()
        items = order.orderitem_set.all()

        for item in items:
            try:
                inventory_item = InventoryItem.objects.get(name=item.menu_item.name)
                if inventory_item.quantity < item.quantity:
                    return Response({
                        'error': f"Stock insuffisant pour {item.menu_item.name}"
                    }, status=status.HTTP_400_BAD_REQUEST)

                inventory_item.quantity -= item.quantity
                inventory_item.save()

            except InventoryItem.DoesNotExist:
                return Response({
                    'error': f"{item.menu_item.name} n'existe pas dans l'inventaire"
                }, status=status.HTTP_400_BAD_REQUEST)

        order.is_completed = True
        order.save()

        return Response({'message': 'Commande traitée avec succès ✅'})

# Items de commande
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
