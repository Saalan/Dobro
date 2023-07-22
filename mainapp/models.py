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

class parsec_dns(models.Model):
    class Meta:
        db_table = 'parsec_dns'
        verbose_name = 'PARSEC_DNS'
        verbose_name_plural = 'PARSEC_DNS'
    id = models.AutoField(primary_key=True, verbose_name='ID')
    id_count_start = models.SmallIntegerField()
    id_request_name = models.SmallIntegerField()
    responce_name = models.CharField(max_length=128)
    ttl = models.IntegerField(null=True)
    ipv4 = CidrAddressField()
    redirect_port = models.IntegerField(null=True)
    rec_time = models.DateTimeField(null=True)

    objects = NetManager()

    def __str__(self):
        return self.responce_name

#class ipv4_device(models.Model):
#    class Meta:
#        db_table = 'ipv4_device'
#        verbose_name = 'DHCP conf'
#        verbose_name_plural = 'DHCP conf(s)'
#    id = models.AutoField(primary_key=True, verbose_name='ID')
#    id_unit = models.IntegerField()
#    id_type = models.IntegerField()
#    id_net_config = models.SmallIntegerField(default='0')
#    mac = MACAddressField()
#    ipv4 = CidrAddressField()
#
#    host_name = models.CharField(max_length=63)
#    comments = models.TextField(max_length=1024)
#    time = models.DateTimeField(auto_now_add=True, blank=True)
#
#    objects = NetManager()
#
#    def __str__(self):
#        return self.host