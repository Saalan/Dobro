from django.db import models
from netfields import CidrAddressField, MACAddressField, NetManager

# pip install django-netfields
# Create your models here.

class arp(models.Model):
    class Meta:
        db_table = 'arpalert_log'
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=True)
    mac = MACAddressField(null=True)
    ipv4 = CidrAddressField(null=True)
    vendor = models.CharField(null=True, max_length=100)

    objects = NetManager()