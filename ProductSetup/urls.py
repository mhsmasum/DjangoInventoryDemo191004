from django.contrib import admin
from django.urls import path , re_path
from django.conf.urls import url
from ProductSetup.views  import  (
    Index,
    NewProduct,
    SaveProduct,
    )

    


urlpatterns = [
    path('index', Index , name='index'),
    path('new', NewProduct , name='new'),
    path('SaveProduct', SaveProduct , name='SaveProduct'),
    


]
urlpatterns+=[


]


