"""Mangolicious URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MangoliciousApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('buynow',views.buynow, name='buynow'),
    path("details",views.details,name='details'),
    path("payment",views.payment,name='payment'),
    # path("details2",views.details2,name='details2'),
    path("paymen2",views.paymen2,name='paymen2'),
    path("cod",views.cod,name='cod'),
    path("coddetails",views.coddetails,name='coddetails'),
    path('proceed-to-pay',views.razorpaycheck,name="proceed-to-pay"),
]
admin.site.site_header  =  "Mangolicious"
admin.site.site_title  =  " admin site"
admin.site.index_title  =  "Mangolicious Admin Panel"  