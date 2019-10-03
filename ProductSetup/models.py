from django.db import models
from BasicSettings.models import *

# Create your models here.
class ProductInfo (models.Model):
    ProductName =  models.CharField(max_length=800,blank=False)
    ProductDescripTion = models.CharField(max_length=5000,blank=False)
    ProductSpecification = models.CharField(max_length=8000,blank=False)
    
    ProductCountry = models.ForeignKey(CountryOrigin , on_delete=models.CASCADE)
    ProductCategory = models.ForeignKey(ItemCategory , on_delete=models.CASCADE)
    ProductBrand = models.ForeignKey(ItemBrand , on_delete=models.CASCADE , blank=True)
    ProductColor = models.ManyToManyField(ItemColor,blank=True,null=True)
    
    ProductSize = models.ManyToManyField(ItemSize,blank=True,null=True)
    ProductUOM = models.ForeignKey(UomMaster , on_delete=models.CASCADE)
    ProductCode = models.CharField(max_length=100,blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True)

    DeleteDate = models.DateTimeField( blank=True, null=True)
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True)

    
    

