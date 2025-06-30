from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)  # ✅ CHAMP AJOUTÉ

    def __str__(self):
        return f"Table {self.number}"

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.date_time}"

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    threshold = models.IntegerField(default=5)  # pour alerte

    def __str__(self):
        return self.name

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Commande {self.id} - Table {self.table.number}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"
