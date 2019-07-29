from django.db import models

# Create your models here.

FREIGHT_CHOICES = (
    ('air', 'AIR'),
    ('sea', 'SEA'),
    ('road', 'ROAD'),
)

TYPE_CHOICES = (
    ('Mineral', 'MINERAL'),
    ('fresh_food', 'FRESH FOOD'),
    ('Medicine', 'MEDICINE'),
)


class freightRate(models.Model):
    Source = models.CharField(max_length=254, default='')
    Destination = models.CharField(max_length=254, default='')
    Port_freight = models.CharField(max_length=254, choices=FREIGHT_CHOICES, default='')
    From_source_to_Port_freight = models.CharField(max_length=254, choices=FREIGHT_CHOICES, default='')
    From_port_to_destination_freight = models.CharField(max_length=254, choices=FREIGHT_CHOICES, default='')
    metric = models.CharField(max_length=254, default='')
    MiniQuantitySent = models.IntegerField(default=1)
    MaxQuantitySent = models.IntegerField(default=1)
    MiniQuantityRecieved = models.IntegerField(default=1)
    MaxQuantityRecieved = models.IntegerField(default=1)
    Total_cost = models.IntegerField(default=1)
    Unit_cost = models.IntegerField(default=1)
    Sourcetax = models.IntegerField(default=1)
    Destinationtax = models.IntegerField(default=1)
    Sourceothertax = models.IntegerField(default=1)
    Destinationothertax = models.IntegerField(default=1)
    MarkupRate = models.IntegerField(default=1)
    Product_types = models.CharField(max_length=254, choices=TYPE_CHOICES, default='')
    DestinAgent = models.CharField(max_length=254, default='')
    OriginAgent = models.CharField(max_length=254, default='')
