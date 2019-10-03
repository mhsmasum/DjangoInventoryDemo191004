from django.contrib import admin
from django.urls import path , re_path
from django.conf.urls import url
from BasicSettings.views  import  *


    

#(?P<slug>[\w-]+)/$
app_name = 'basic'
urlpatterns = [
    
    path('uom', UomSetup , name='uom'),
    path('addUomDetailsFormRow' ,addUomDetailsFormRow  ,  name='addUomDetailsFormRow'),
    path('SaveUom' ,SaveUom  ,  name='SaveUom'),
    path('EditUom' ,EditUom  ,  name='EditUom'),
    path('UpdateUom' ,UpdateUom,name='UpdateUom' ),
    path('uomInfo/<int:uom>/' ,EditUom  ,  name='uomInfo'),
    path('UomList' ,UomListView.as_view(),name='UomList' ),
    path('GetUomDetailsByMaster' ,GetUomDetailsByMaster,name='GetUomDetailsByMaster' ),

    #region ItemGroup

    path('newgroup', NewGroup , name='NewGroup'),
    path('SaveGroup', SaveGroup , name='SaveGroup'),
    path('groups', GroupList.as_view() , name='groups'),
    path('EditGroup/<int:group>/', EditGroup , name='EditGroup'),
    path('UpdateGroup', UpdateGroup , name='UpdateGroup'),

    #end region

    #region Item Category
    path('newcategory', NewCategory , name='newcategory'),
    path('SaveCategory', SaveCategory , name='SaveCategory'),
    path('UpdateCategory', UpdateCategory , name='UpdateCategory'),
    
    path('category/<int:cat>/', EditCategory , name='category'),
    path('categories', CategoryListView.as_view() , name='categories'),
    #endregion

    #region Item Brand
    path('newbrand', NewBrand , name='newbrand'),
    path('SaveBrand', SaveBrand , name='SaveBrand'),
    path('brands', BrandListView.as_view() , name='brands'),
    path('brand/<int:brand>/', EditBrand , name='brand'),
    path('UpdateBrand', UpdateBrand , name='UpdateBrand'),

    #endregion

    #regiom Item Color
    path('newcolor', NewColor , name='newcolor'),
    path('SaveColor', SaveColor , name='SaveColor'),
    path('colors', ColorListView.as_view() , name='colors'),
    path('colorE/<int:color>/', EditColor , name='colorE'),
    path('UodateColor', UodateColor , name='UodateColor'),


    #endregion

    #regiom Item Size
    path('newsize', NewSize , name='newsize'),
    path('SaveSize', SaveSize , name='SaveSize'),
    path('sizes', SizeListView.as_view() , name='sizes'),
    path('size/<int:size>/', EditSize , name='size'),
    path('UodateSize', UodateSize , name='UodateSize'),


    #endregion
    
    

    
 

    







]
urlpatterns+=[


]


