from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse, Http404
from .models import BuyNow, RipeMangoes
from .models import Details
from .models import Cod
from django.shortcuts import redirect
import os
from django.conf import settings


def download_brochure(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'mangoliciousbroucher.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path,'rb'), content_type = "application/pdf")
    else:
        return Http404("File Not Found")


# Create your views here.

def index(request):
    cc = Details.objects.count()
    print(cc)
    return render(request, "index.html", {'cc':cc})

def about(request):
    return render(request, "aboutus.html")

def rawmangoes(request):
    buy = BuyNow.objects.all()
    print(buy)
    return render(request, "buynow.html", {'buy':buy})

def ripemangoes(request):
    buy = RipeMangoes.objects.all()
    print(buy)
    return render(request, "ripe-mangoes.html", {'buy':buy})

def cod(request):
    if request.method == "POST":
        username = request.POST['username'] 
        mail = request.POST['email']
        Mo_no = request.POST['mono']
        quantt = request.POST['quantity']
        Choice = request.POST['choices']
        city = request.POST['city']
        typeofmangoes = request.POST['typeofmangoes']
        add = request.POST['address']
        new_data = Cod(name=username, email = mail, Mo_No = Mo_no, quant = quantt,Choice= Choice, city=city,typeofmangoes=typeofmangoes, address = add)
        new_data.save()
        return redirect(coddetails)
    return render(request,'cod.html')

def details(request):
    if request.method == "POST":
        username = request.POST['username'] 
        mail = request.POST['email']
        Mo_no = request.POST['mono']
        quantt = request.POST['quantity']
        Choice = request.POST['choices']
        city = request.POST['city']
        typeofmangoes = request.POST['typeofmangoes']
        add = request.POST['address']
        new_data = Details(name=username, email = mail, Mo_No = Mo_no, quant = quantt,Choice= Choice, city=city,typeofmangoes=typeofmangoes, address = add)
        new_data.save()
        return redirect(payment)
    return render(request, "details.html")

def coddetails(request):
    detail = Cod.objects.all().values('city').latest('id')
    vv = detail.get('city')
    print(vv)
    CityPrice = BuyNow.objects.all().values(vv)
    for cc in CityPrice:
        cp = cc[vv]
    boxes = Cod.objects.all().values('quant').latest('id')
    bb = boxes.get('quant')
    print(bb)

    tot = cp * bb
    print(tot)
    return render(request,"coddetails.html",{'tot':tot,'vv':vv,'cp':cp,'bb':bb})

def payment(request):
    detail = Details.objects.all().values('city').latest('id')
    vv = detail.get('city')
    print(vv)
    CityPrice = BuyNow.objects.all().values(vv)
    for cc in CityPrice:
        cp = cc[vv]
    boxes = Details.objects.all().values('quant').latest('id')
    bb = boxes.get('quant')
    print(bb)

    tot = cp * bb

    totalindb = Details.objects.latest('id')
    totalindb.total_price = tot
    totalindb.save()
    print(tot)


    return render(request,"payment.html",{'tot':tot,'vv':vv,'cp':cp,'bb':bb})

def razorpaycheck(request):
    detail = Details.objects.all().values('city').latest('id')
    vv = detail.get('city')
    print(vv)
    CityPrice = BuyNow.objects.all().values(vv)
    for cc in CityPrice:
        cp = cc[vv]
    boxes = Details.objects.all().values('quant').latest('id')
    bb = boxes.get('quant')
    print(bb)

    tot = cp * bb
    print(tot)

    return JsonResponse({
        'total_price':tot
    })
def paymen2(request):

    return render(request,"paymen2.html")

def message(request):
    return render(request,"message.html")

