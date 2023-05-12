from django.shortcuts import render
from Ecartshop.models import Product
from django.db.models import Q

# Create your views here.
def searchresult(request):
    Products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) |  Q(desc__contains=query))
        return render(request,'searchapp.html',{'query':query,'Product':products})