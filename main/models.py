from django.core.exceptions import DisallowedHost
from django.db import models

class Trades(models.Model):
    name = models.CharField(max_length=100)
    
