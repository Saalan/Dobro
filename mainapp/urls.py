from django.urls import path
from . import views


urlpatterns = [
    path('', views.common, name="common"),
    path('arp-log', views.arp_log, name="arp-log"),
    path('dhcpd-conf', views.dhcpd_conf, name="dhcpd-conf"),
    path('named-conf', views.named_conf, name="named-conf"),
]