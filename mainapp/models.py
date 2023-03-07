from django.db import models
from netfields import CidrAddressField, MACAddressField, NetManager

# pip install django-netfields
# Create your models here.

class arpalert_log(models.Model):
    class Meta:
        db_table = 'arpalert_log'
        verbose_name = 'ARP лог'
        verbose_name_plural = 'ARP логи'
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=True)
    mac = MACAddressField(null=True)
    ipv4 = CidrAddressField(null=True)
    vendor = models.CharField(null=True, max_length=100)

    objects = NetManager()

    def __str__(self):
        return self.vendor