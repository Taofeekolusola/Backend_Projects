from django.db import models

# Box States
BOX_STATES = [
    ('IDLE', 'Idle'),
    ('LOADING', 'Loading'),
    ('LOADED', 'Loaded'),
    ('DELIVERING', 'Delivering'),
    ('DELIVERED', 'Delivered'),
    ('RETURNING', 'Returning'),
]

class Box(models.Model):
    txref = models.CharField(max_length=20, unique=True)
    weight_limit = models.FloatField(default=500)  # Max weight in grams
    battery_capacity = models.FloatField()  # Battery percentage
    state = models.CharField(max_length=10, choices=BOX_STATES, default='IDLE')

    def __str__(self):
        return self.txref

class Item(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()  # Weight in grams
    code = models.CharField(max_length=100, unique=True, default=1)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name