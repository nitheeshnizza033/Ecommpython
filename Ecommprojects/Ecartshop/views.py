from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

def AllProductcat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Product.objects.all().filter(category=c_page,stock_avail=True)
    else:
        products_list=Product.objects.all().filter(stock_avail=True)
    paginator=Paginator(products_list,9)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,'Category.html',{'Category':c_page,'Product':products})

def proddetail(request,c_slug,Product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=Product_slug)
    except Exception as e:
        raise e
    return render(request,'proddetail.html',{'Product':product})


