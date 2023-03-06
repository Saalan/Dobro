from django.shortcuts import render
from django.http import HttpResponse


def common(request):
    return render(request, "mainapp/common.html")


def arp_log(request):
    return render(request, "mainapp/arp-log.html")


def dhcpd_conf(request):
    return render(request, "mainapp/dhcpd-conf.html")


def named_conf(request):
    return render(request, "mainapp/named-conf.html")