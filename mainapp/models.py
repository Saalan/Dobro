from django.db import models
from netfields import CidrAddressField, MACAddressField, NetManager

# pip install django-netfields
# Create your models here.

class arpalert_log(models.Model):
    class Meta:
        db_table = 'arpalert_log'
        verbose_name = 'ARP лог'
        verbose_name_plural = 'ARP логи'
    id = models.AutoField(primary_key=True, verbose_name='ID')
    time = models.DateTimeField(null=True)
    mac = MACAddressField(null=True)
    ipv4 = CidrAddressField(null=True)
    vendor = models.CharField(null=True, max_length=100)

    objects = NetManager()

    def __str__(self):
        return self.vendor

class net_device(models.Model):
    class Meta:
        db_table = 'net_device'
        verbose_name = 'DHCP conf'
        verbose_name_plural = 'DHCP conf'
    id = models.AutoField(primary_key=True, verbose_name='ID')
    cfg_id = models.IntegerField()
    group = models.SmallIntegerField(default='0')
    mac = MACAddressField()
    ipv4 = CidrAddressField()
    host = models.CharField(max_length=63)
    comments = models.TextField(max_length=1024)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    objects = NetManager()

    def __str__(self):
        return self.host