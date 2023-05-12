
from django.urls import path, include
from .import views
app_name='Ecartshop'
urlpatterns = [

    path('',views.AllProductcat,name='AllProductcat'),
    path('<slug:c_slug>/',views.AllProductcat,name='Product_By_Category'),
    path('<slug:c_slug>/<slug:Product_slug>/',views.proddetail,name='prodCategorydetail'),
    ]