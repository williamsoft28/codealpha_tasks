from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MenuItem, Table, Reservation, InventoryItem, Order, OrderItem

admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(InventoryItem)
admin.site.register(Order)
admin.site.register(OrderItem)
