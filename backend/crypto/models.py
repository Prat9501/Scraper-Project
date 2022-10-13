from django.db import models

class CurrencyData(models.Model):
    image_link = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    time_1h = models.CharField(max_length=50)
    time_24h = models.CharField(max_length=50)
    time_7d = models.CharField(max_length=50)
    market_cap = models.CharField(max_length=50)
    volume_by_price = models.CharField(max_length=50)
    volume_by_units = models.CharField(max_length=50)
    supply = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.name