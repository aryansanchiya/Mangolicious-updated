from django.urls import path
from . import views

urlpatterns = {
    path("",views.index,name='index'),
    path("about",views.about,name='about'),
    path("buynow",views.buynow,name='buynow'),
    path("details",views.details,name='details'),
    path("payment",views.payment,name='payment'),
    path("coddetails",views.coddetails,name='coddetails'),
    path('proceed-to-pay',views.razorpaycheck,name="proceed-to-pay"),
    # path('')
}