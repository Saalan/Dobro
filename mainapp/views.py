from django.shortcuts import render
from .models import arpalert_log
from .models import parsec_dns


def common(request):
    return render(request, "mainapp/common.html")


def arp_log(request):
    arp_logs = arpalert_log.objects.order_by('-id')
    return render(request, "mainapp/arp-log.html", { 'arp_logs': arp_logs})


def dhcpd_conf(request):
    return render(request, "mainapp/dhcpd-conf.html")


def named_conf(request):
    return render(request, "mainapp/named-conf.html")


def parsec_db(request):
    parsec_db = parsec_dns.objects.order_by('-id')
    return render(request, "mainapp/parsec-db.html", { 'parsec_db': parsec_db})