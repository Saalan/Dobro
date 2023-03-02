from django.shortcuts import render
from django.http import HttpResponse


def common(request):
    return render(request, "mainapp/common.html")


def arplog(request):
    return HttpResponse("<h4>Hello</h4>")





#   return render(request, "mainapp/common.html")
#   return render(request, "mainapp/index.html")
