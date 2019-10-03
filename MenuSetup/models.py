from django.db import models

# Create your models here.


class MenuStepOne(object):
    MenuName =None 
    UrlName = None
    MenuType =None
    AppMenu = None
    MenuStepTwoList = None
    
    def __init__(self , menuName , urlName , menuType ,  appMenu ):
        self.MenuName =menuName 
        self.UrlName = urlName
        self.MenuType =menuType
        self.AppMenu = appMenu
        self.MenuStepTwoList = self.GetMenuStepTwo()
    def GetMenuStepTwo(self):
        asd = self
        menuStep = AppMenu.objects.filter(IsActive=True,IsDelete=False , ParentMenu=self.AppMenu)
        menuStep = list(menuStep)
        menuStepTwo = []
        for menu in menuStep:
            menuStep = MenuStepTwo(menuName = menu.MenuName , urlName = menu.UrlName , menuType = menu.MenuType , appMenu = menu.id )
            
            menuStepTwo.append(menuStep)
        return menuStepTwo
    


class MenuStepTwo(object):
    MenuName =None 
    UrlName = None
    MenuType =None
    ParentMenu =None
    MenuStepThreeList = None

    def __init__(self , menuName , urlName , menuType ,  appMenu ):
        self.MenuName =menuName 
        self.UrlName = urlName
        self.MenuType =menuType
        self.ParentMenu =None
        self.AppMenu = appMenu
        self.MenuStepThreeList =  self.GetMenuStepThree()
    def GetMenuStepThree(self):
        asd = self
        menuStep = AppMenu.objects.filter(IsActive=True,IsDelete=False , ParentMenu=self.AppMenu)
        menuStep = list(menuStep)
        menuStepthree = []
        for menu in menuStep:
            menuStep = MenuStepThree(menuName = menu.MenuName , urlName = menu.UrlName , menuType = menu.MenuType , appMenu = menu.id )
            
            menuStepthree.append(menuStep)
        return menuStepthree

class MenuStepThree(object):
    MenuName =None 
    UrlName = None
    MenuType =None
    ParentMenu =None
    AppMenu = None
   

    def __init__(self, menuName , urlName , menuType ,  appMenu):
        self.MenuName =menuName 
        self.UrlName = urlName
        self.MenuType =menuType
        self.ParentMenu =None
        self.AppMenu = appMenu
        


class MenuType(models.Model):
    MeneType = models.CharField(max_length=800,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True)
    DeleteDate = models.DateTimeField( blank=True, null=True)
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True)
    def __str__ (self):
        return self.MeneType
class MenuStep (models.Model):
    StepCount =models.IntegerField(unique=True)
    StepName =models.CharField(max_length=50,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True)
    def __str__ (self):
        return self.StepName+'|'+str(self.StepCount)
    


class AppMenuManager(models.Manager):
    def GetAppMenu(self , pk):
        qs = self.get_queryset().filter(pk = pk)
        if qs.count()==1:
            return  qs.first
        return  None
    
class AppMenu(models.Model):
    MenuName =  models.CharField(max_length=800,blank=False)
    UrlName =  models.CharField(max_length=800,null=True , blank=True)
    OrderNo = models.IntegerField(default=0)
    MenuStep = models.ForeignKey(MenuStep , on_delete=0 )
    MenuType = models.ForeignKey(MenuType , on_delete=0)
    ParentMenu = models.IntegerField(default=0)
    IsActive = models.BooleanField(default=True,blank=False)
    IsDelete = models.BooleanField(default=False,blank=False)
    CreateDate = models.DateTimeField(auto_now_add=True , blank=True)
    CreateBy = models.CharField(max_length=500 , blank=True)
    UpdateBy = models.CharField(max_length=500 , blank=True,null=True)
    UpdateDate = models.DateTimeField(auto_now=True,blank=True,null=True)
    DeleteDate = models.DateTimeField( blank=True, null=True)
    DeleteBy = models.CharField(max_length=500 , blank=True,null=True)
    objects = AppMenuManager()

    def __str__(self):
        
        return self.MenuName+'|'+('' if self.UrlName is None else self.UrlName)+  '| Default' if self.OrderNo==0 else str(self.OrderNo)

    def GetMenuStepOne(path):
        menuStepOne = []
        menuStep = AppMenu.objects.filter(IsActive=True,IsDelete=False , MenuStep=1)
        appMenu = list(menuStep)
        
        for menu in appMenu:
            apath = path
            asd = menu.UrlName
            menuStep = MenuStepOne(menuName = menu.MenuName , urlName = menu.UrlName , menuType = menu.MenuType , appMenu = menu.id )
            
            menuStepOne.append((menuStep))
        return menuStepOne


   
        