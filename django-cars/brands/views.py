from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Car, Brand

def default_page(request):
    return HttpResponse("Hellothere")
# Create your views here.
def all_brands(request):
    all_brands=Brand.objects.all()
    data={'all_brands':all_brands}
    # for x in data['all_brands']:
    #     print(x.name)
    # print(data['all_brands'])
    return render(request, "all_brands.html", data)

def new_brand(request):
    print(request.POST['name'])
    new_brand=Brand(name=request.POST['name'])
    new_brand.save()
    return HttpResponseRedirect("/brands")

def one_brand(request, brand_id):
    data={}
    try:
        our_brand=Brand.objects.get(id=brand_id)
        data['our_brand']=our_brand
        data['cars']=[]
        for x in our_brand.cars.all():
            data['cars'].append(x)
    except:
        pass
    return render(request, "one_brand.html", data)

def one_car(request, brand_id, car_id):
    data={}
    try:
        our_brand=Brand.objects.get(id=brand_id)
        data['our_brand']=our_brand
        car=Car.objects.get(id=car_id)
        data['car']=car
        print(car.brand)
    except:
        pass
    return render(request, "one_car.html", data)