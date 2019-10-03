from django.db import models

class ItemGroupManager(models.Manager):
    def GetItemGroup(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None

class ItemGroup(models.Model):
    ItemGroupName = models.CharField(max_length=120)
    GroupShortName = models.CharField(max_length=5  )
    IsActive = models.BooleanField(default=True)
    IsDelete = models.BooleanField(default=False)
    CreateBy = models.CharField(max_length=500  )
    CreateDate = models.DateTimeField(auto_now_add=True )
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True )
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True )
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True )
    objects = ItemGroupManager()

    def __str__(self):

        return  self.ItemGroupName+':'+self.GroupShortName




    
#endregion

#region ItemCategory
class ItemCategoryManager(models.Manager):
    def GetItemCategory(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None
class ItemCategory(models.Model):
    ItemGroup = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    ItemCategory = models.CharField(max_length=120)
    CategoryShortName = models.CharField(max_length=5  )
    IsDelete = models.BooleanField(default=False)
    CreateBy = models.CharField(max_length=500  )
    CreateDate = models.DateTimeField(auto_now_add=True  )
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True )
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True )
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True )
    IsActive = models.BooleanField(default=True)
    objects = ItemCategoryManager()


    def __str__(self):

        return  self.ItemCategory+':'+self.CategoryShortName
#endregion

class UomMasterManager(models.Manager):
    def GetUomMasterId(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None
class UomMaster(models.Model):
    UomMasterName =  models.CharField(max_length=500)
    UomMasterShortName =  models.CharField(max_length=500)
    IsActive = models.BooleanField(default=True)
    IsDelete = models.BooleanField(default=False)
    CreateBy = models.CharField(max_length=500 , blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    UpdateBy = models.CharField(max_length=500 , blank=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True)
    DeleteBy = models.CharField(max_length=500 , blank=True)
    objects = UomMasterManager()
    
    def __str__(self):

        return  self.UomMasterName
    


class UomDetailsManager(models.Manager):
    def GetUomDetailsId(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None
    
        

class UomDetails(models.Model):
    UomMaster = models.ForeignKey(UomMaster, on_delete=models.CASCADE)
    UomDetailsName = models.CharField(max_length=500,blank=False)
    UomDetailsShortName = models.CharField(max_length=500 , blank=False)
    ConversionValue = models.DecimalField(max_digits=18, decimal_places=3, default=1,blank=False)
    EqualToMaster = models.BooleanField(default=False , blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    objects = UomDetailsManager()
    
    

    def __str__(self):

        return  self.UomDetailsName+':'+self.UomDetailsShortName

class UomDetailsUpdateLog(models.Model):
    UomDetails = models.ForeignKey(UomDetails,on_delete=models.SET_NULL,null=True)
    UomMaster = models.ForeignKey(UomMaster,on_delete=models.SET_NULL,null=True)
    UomDetailsName = models.CharField(max_length=500,blank=False)
    UomDetailsShortName = models.CharField(max_length=500 , blank=False)
    ConversionValue = models.DecimalField(max_digits=18, decimal_places=3, default=1,blank=False)
    EqualToMaster = models.BooleanField(default=False , blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)



class ItemBrandManager(models.Manager):
    def GetItemBrand(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None
class ItemBrand(models.Model):
    ItemBrandName =  models.CharField(max_length=500,blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    DeleteDate = models.DateTimeField( null=True ,blank=True)
    DeleteBy = models.CharField(max_length=500 , blank=True , null = True)
    UpdateBy = models.CharField(max_length=500 , blank=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True)
    objects = ItemBrandManager()
    
    
    def __str__(self):

        return  self.ItemBrandName

class ItemColorManager(models.Manager):
    def GetItemColor(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None

class ItemColor(models.Model):
    ItemColorName =  models.CharField(max_length=500,blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    DeleteDate = models.DateTimeField(  blank=True , null = True)
    DeleteBy = models.CharField(max_length=500 , blank=True , null = True)
    UpdateBy = models.CharField(max_length=500 , blank=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True)
    objects = ItemColorManager()
      
    def __str__(self):

        return  self.ItemColorName


class ItemSizeManager(models.Manager):
    def GetItemSize(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None
class ItemSize(models.Model):
    ItemSizeName =  models.CharField(max_length=1000,blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    DeleteDate = models.DateTimeField(  blank=True , null=True)
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True)
    UpdateBy = models.CharField(max_length=500 , blank=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True)
    objects = ItemSizeManager()
      
    def __str__(self):

        return  self.ItemSizeName


class CountryOriginManager(models.Manager):
    def GetItemCountry(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None


class CountryOrigin(models.Model):
    CountryName = models.CharField(max_length=500,blank=False)
    CountryShortName = models.CharField(max_length=5,blank=False)
    IsActive = models.BooleanField(default=True,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    UpdateBy = models.CharField(max_length=500 , blank=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True)
    DeleteDate = models.DateTimeField(  blank=True)
    DeleteBy = models.CharField(max_length=500 , blank=True)
    objects = CountryOriginManager()

    def __str__(self):
        return  self.CountryName

    


