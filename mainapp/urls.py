from django.urls import path
from . import views

urlpatterns = [
    path('', views.common, name="common"),
#     path('', views.common),
]
