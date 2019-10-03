from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from django.template import loader
from django.template.loader import render_to_string
from django.urls import reverse
from .forms import *
from .models import UomMaster , UomDetails ,UomDetailsUpdateLog , ItemGroup,ItemCategory
import json
from django.db import DatabaseError, transaction ,IntegrityError
from Utility.AppError import AppError
from Utility.ResultResponse import ResultResponse

from django.views.generic import ListView, DetailView
from django.core import serializers

def homeView(request):
    context={'test':"This Is A Test"}
    return render(request , 'BasicSettings/homeView.html',context)

def UomSetup(request): 


    masterForm = UomMasterForm( None)
    detailForm = UomDetailsForm( None)
    context = {
        'masterForm':masterForm,
        'detailForm':detailForm,
    }
    
    return render(request, 'BasicSettings/UomSetup.html', context)

def SaveUom(request):
    aResponse = ResultResponse()


    received_json_data = json.loads(request.body.decode("utf-8"))
    
    details = received_json_data.pop('UomDetails' or None)
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    

    name = received_json_data.get('UomMasterName')
    shortName = received_json_data.get('UomMasterShortName')
    active = received_json_data.get('IsActive')
    
   
    CreateBy = 'admin'
   
    
    masterForm = UomMasterForm( theRequest.POST or None )
    if masterForm.is_valid():
        aResponse.IsSuccess=False
        amaster =  UomMaster(UomMasterName =name  , UomMasterShortName = shortName , IsActive = active ,CreateBy = CreateBy )
        with transaction.atomic():
            try:
                amaster.save()
                for theDetails in details:
                    uomDetails = UomDetails.objects.create(
                        UomMaster = amaster , 
                        UomDetailsName =theDetails['UomDetailsName'], 
                        UomDetailsShortName = theDetails['UomDetailsShortName'] ,
                        ConversionValue = theDetails['ConversionValue'] ,
                        EqualToMaster = theDetails['EqualToMaster'] ,
                        IsActive = True
                        )
                    uomDetails.save()
                aResponse.IsSuccess=True
            except Exception as ex:
                aResponse.IsSuccess=False
                aResponse.ErrorMessage = ex.args
                transaction.set_rollback(True)
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
            
    else:
        
        appError = AppError()

        template = render_to_string('BasicSettings/_uomMasterForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)
        




def addUomDetailsFormRow(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data
    trCount = received_json_data.get('trCount')

    detailForm = UomDetailsForm(theRequest.POST )
  
    if detailForm.is_valid():
        aResponse.IsSuccess = True
        context  = {
            'detailForm':detailForm ,
            'trCount':trCount  
        }
        template = render_to_string('BasicSettings/_uomDetailsFromRow.html' , context  )
        aResponse.TheData = str(template)
        #return HttpResponse(template)
        return JsonResponse(json.dumps(aResponse.__dict__ ) , safe=False)
    else:
        appError = AppError()

        
        template = render_to_string('BasicSettings/_uomDetailsForm.html' , {'detailForm':detailForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)




def EditUom(request , uom):
    
    context = {}
    uomMaster = UomMaster.objects.get(pk=uom)
    
    masterForm = UomMasterForm( instance = uomMaster)
    detailForm = UomDetailsForm(instance = None)
    context = {
        'masterForm':masterForm,
        'detailForm':detailForm,
        'masterId':uom,
        }
        
    return render(request, 'BasicSettings/uomEdit.html' , context)


def GetUomDetailsByMaster(request):

    data = request.GET
    uomMasterId = int(request.GET.get('uomMasterId'))
    
    details  = UomDetails.objects.filter(UomMaster=uomMasterId)
    detailsList  = serializers.serialize("json", list(details))
    return HttpResponse(detailsList, content_type='application/json')


def UpdateUom(request):
    aResponse = ResultResponse()


    received_json_data = json.loads(request.body.decode("utf-8"))
    
    newDetails = received_json_data.pop('UomDetails' or None)
    
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data
    
    name = received_json_data.get('UomMasterName')
    uomid = received_json_data.get('id')
    shortName = received_json_data.get('UomMasterShortName')
    active = received_json_data.get('IsActive')


    uomMaster = UomMaster.objects.get(pk=int(uomid))
    uomMaster.UomMasterName = name
    uomMaster.UomMasterShortName = shortName
    uomMaster.IsActive = active
    uomMaster.save()

    detailsList  = UomDetails.objects.filter(UomMaster=int(uomid))
    updateList = []
    uomDetailsList=[]
    for details in detailsList:
        update = UomDetailsUpdateLog( 
            UomDetails = details , 
            UomMaster = uomMaster,
            UomDetailsName = details.UomDetailsName,
            UomDetailsShortName = details.UomDetailsShortName,
            ConversionValue = details.ConversionValue,
            EqualToMaster = details.EqualToMaster,
            IsActive = details.IsActive,
            CreateBy='admin'
            )
        
        updateList.append(update)

    for theDetails in newDetails:
        uomDetails = UomDetails.objects.create(
            UomMaster = uomMaster , 
            UomDetailsName =theDetails['UomDetailsName'], 
            UomDetailsShortName = theDetails['UomDetailsShortName'] ,
            ConversionValue = theDetails['ConversionValue'] ,
            EqualToMaster = True if theDetails['EqualToMaster']=="True" else False ,
            IsActive = True
            )
        uomDetailsList.append(uomDetails)   
    masterForm = UomMasterEditForm(theRequest.POST,instance = uomMaster )
    if masterForm.is_valid():
        UomDetailsUpdateLog.objects.bulk_create(updateList)
        UomDetails.objects.filter(UomMaster=int(uomid)).delete()
        UomDetails.objects.bulk_create(uomDetailsList)   
        aResponse.IsSuccess = True
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        
        
        appError = AppError()

        template = render_to_string('BasicSettings/_uomMasterEditForm.html' , {'masterEditForm':masterForm  } )
        appError.TheData = str(template)
        
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)

    
def NewGroup(request):
    masterForm = ItemGroupForm( None)
    
    context = {
        'masterForm':masterForm
        
    }
    
    return render(request, 'BasicSettings/ItemGroupCreate.html', context)

    
def SaveGroup(request):
    aResponse = ResultResponse()

    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True

    theRequest.POST=received_json_data
    name = received_json_data.get('ItemGroupName')
    shortName = received_json_data.get('GroupShortName')
    active = received_json_data.get('IsActive')
    masterForm = ItemGroupForm(theRequest.POST)
    if masterForm.is_valid():
        
        item = ItemGroup(ItemGroupName = name ,GroupShortName = shortName, IsActive = active , CreateBy='Admin')
        item.save()
        if item.pk>0:
            aResponse.IsSuccess = True
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_itemGroupForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)



def EditGroup(request , group):
    context = {}
    item = ItemGroup.objects.get(pk=group)
    masterForm = ItemGroupForm( instance = item  )
    detailForm = UomDetailsForm( None)
    
    context = {
        'masterForm':masterForm,
        'masterId':group,    
        }
    return render(request, 'BasicSettings/EditGroup.html' , context)

def UpdateGroup(request):
    aResponse = ResultResponse()

    received_json_data = json.loads(request.body.decode("utf-8"))
    
    
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data
    
    name = received_json_data.get('ItemGroupName')
    shortName = received_json_data.get('GroupShortName')
    active = received_json_data.get('IsActive')
    groupId = received_json_data.get('id')
    aResponse = ResultResponse()

    group = ItemGroup.objects.get(id=int(groupId))
    masterForm = ItemGroupForm(theRequest.POST , instance = group)
    if masterForm.is_valid():
        
        group.ItemGroupName = name
        group.GroupShortName = shortName
        group.UpdateBy='admin'
        group.IsActive = active
        group.save()
        aResponse.IsSuccess = True
    
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_itemGroupForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)
        



def NewCategory(request):
    
    masterForm = ItemCategoryForm()

    context = {
        'masterForm':masterForm
        
    }
    
    return render(request, 'BasicSettings/NewCategory.html', context)

def SaveCategory(request):

    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    
    theRequest.POST=received_json_data

    group =  received_json_data.get('ItemGroup') 
    name = received_json_data.get('ItemCategory')
    shortName = received_json_data.get('CategoryShortName')
    active = received_json_data.get('IsActive')

    masterForm = ItemCategoryForm(theRequest.POST)
    if masterForm.is_valid():
       
        category = ItemCategory(ItemGroup = ItemGroup.objects.get(id=int(group)) ,ItemCategory = name,CategoryShortName = shortName  ,IsActive = active , CreateBy='Admin')
        category.save()
        if category.pk>0:
            aResponse.IsSuccess = True
            aResponse.PK = category.pk
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_itemCategoryForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)

def EditCategory(request,cat):
    category = ItemCategory.objects.get(pk = cat)
    masterForm = ItemCategoryForm( instance = category  )
    context = {
        'masterForm':masterForm,
        'masterId':cat,    
        }
    return render(request, 'BasicSettings/EditCategory.html' , context)


def UpdateCategory(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    group =  received_json_data.get('ItemGroup') 
    name = received_json_data.get('ItemCategory')
    shortName = received_json_data.get('CategoryShortName')
    active = received_json_data.get('IsActive')
    categoryId = received_json_data.get('id')
    
    aResponse = ResultResponse()

    category = ItemCategory.objects.get(id=int(categoryId))

    masterForm = ItemCategoryForm(theRequest.POST , instance = category)

    if masterForm.is_valid():
        category.ItemCategory = name
        category.CategoryShortName = shortName
        category.ItemGroup = ItemGroup.objects.get(id=int(group))
        category.IsActive = active
        category.UpdateBy = 'Admin'
        category.save()
        aResponse.IsSuccess = True
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_itemCategoryForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)


def NewBrand(request):
    masterForm = ItemBrandForm(None)
    context = {
        'masterForm':masterForm
    }
    return render(request, 'BasicSettings/NewBrand.html', context)


def SaveBrand(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    brandName =  received_json_data.get('ItemBrandName') 
    
    active = received_json_data.get('IsActive')

    masterForm = ItemBrandForm(theRequest.POST)

    masterForm = ItemBrandForm(theRequest.POST)
    if masterForm.is_valid():
       
        brand = ItemBrand(ItemBrandName = brandName ,IsActive = active , CreateBy='Admin')
        brand.save()
        if brand.pk>0:
            aResponse.IsSuccess = True
            aResponse.PK = brand.pk
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()
        template = render_to_string('BasicSettings/_brandForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)


def EditBrand(request,brand):
    itemBrand = ItemBrand.objects.get(pk = brand)
    masterForm = ItemBrandForm( instance = itemBrand  )
    context = {
        'masterForm':masterForm,
        'masterId':brand,    
        }
    return render(request, 'BasicSettings/EditBrand.html' , context)


def UpdateBrand(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    brandName =  received_json_data.get('ItemBrandName') 
    
    active = received_json_data.get('IsActive')

    brandId = received_json_data.get('id')
    aResponse = ResultResponse()

    brand = ItemBrand.objects.get(id=int(brandId))
    masterForm = ItemBrandForm(theRequest.POST , instance = brand)
    if masterForm.is_valid():
        
        brand.ItemBrandName = brandName
        brand.UpdateBy='admin'
        brand.IsActive = active
        brand.save()
        aResponse.IsSuccess = True
    
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_brandForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)


#regiom Item Color

def NewColor(request):
    masterForm = ItemColorForm(None)
    
    context = {
        'masterForm':masterForm
        
    }
    return render(request, 'BasicSettings/NewColor.html', context)

def SaveColor(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    colorName =  received_json_data.get('ItemColorName') 
    
    active = received_json_data.get('IsActive')

    

    masterForm = ItemColorForm(theRequest.POST)
    if masterForm.is_valid():
       
        color = ItemColor(ItemColorName = colorName ,IsActive = active , CreateBy='Admin')
        color.save()
        if color.pk>0:
            aResponse.IsSuccess = True
            aResponse.PK = color.pk
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()
        template = render_to_string('BasicSettings/_colorForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)



def EditColor(request , color):
    aColor = ItemColor.objects.get(pk = color)
    masterForm = ItemColorForm( instance = aColor  )
    context = {
        'masterForm':masterForm,
        'masterId':color,    
        }
    return render(request, 'BasicSettings/EditColor.html' , context)


def UodateColor(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    colorName =  received_json_data.get('ItemColorName') 
    
    active = received_json_data.get('IsActive')

    colorId = received_json_data.get('id')
    aResponse = ResultResponse()

    aColor = ItemColor.objects.get(id=int(colorId))
    masterForm = ItemColorForm(theRequest.POST , instance = aColor)
    if masterForm.is_valid():
        
        aColor.ItemColorName = colorName
        aColor.UpdateBy='admin'
        aColor.IsActive = active
        aColor.save()
        aResponse.IsSuccess = True
    
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_colorForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)

#endregion



#region Item Size

def NewSize(request):
    masterForm = ItemSizeForm(None)
    
    context = {
        'masterForm':masterForm
        
    }
    return render(request, 'BasicSettings/NewSize.html', context)

def SaveSize(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    sizeName =  received_json_data.get('ItemSizeName') 
    
    active = received_json_data.get('IsActive')

    masterForm = ItemSizeForm(theRequest.POST)
    if masterForm.is_valid():
       
        size = ItemSize(ItemSizeName = sizeName ,IsActive = active , CreateBy='Admin')
        size.save()
        if size.pk>0:
            aResponse.IsSuccess = True
            aResponse.PK = size.pk
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()
        template = render_to_string('BasicSettings/_sizeForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)


def EditSize(request , size):
    aSize = ItemSize.objects.get(pk = size)
    masterForm = ItemSizeForm( instance = aSize  )
    context = {
        'masterForm':masterForm,
        'masterId':size,    
        }
    return render(request, 'BasicSettings/EditSize.html' , context)

def UodateSize(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data

    sizeName =  received_json_data.get('ItemSizeName') 
    
    active = received_json_data.get('IsActive')

    sizeId = received_json_data.get('id')
    aResponse = ResultResponse()

    aSize = ItemSize.objects.get(id=int(sizeId))
    masterForm = ItemSizeForm(theRequest.POST , instance = aSize)
    if masterForm.is_valid():
        
        aSize.ItemSizeName = sizeName
        aSize.UpdateBy='admin'
        aSize.IsActive = active
        aSize.save()
        aResponse.IsSuccess = True
    
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()

        template = render_to_string('BasicSettings/_sizeForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)   

#endregion


class GroupList(ListView):
    template_name = "BasicSettings/GroupList.html"
    def get_queryset(self,*args ,**kwargs):
        qs = ItemGroup.objects.filter(IsDelete = False)         
        return  qs
    




class UomListView(ListView):
    template_name = "BasicSettings/UomList.html"
    def get_queryset(self,*args ,**kwargs):
        querySet = UomMaster.objects.filter(IsDelete = False)             
        return  querySet

class CategoryListView(ListView):
    template_name = "BasicSettings/CategoryList.html"
    def get_queryset(self,*args ,**kwargs):
        querySet = ItemCategory.objects.filter(IsDelete = False)             
        return  querySet

class BrandListView(ListView):
    template_name = "BasicSettings/BrandList.html"
    def get_queryset(self,*args ,**kwargs):
        querySet = ItemBrand.objects.filter(IsDelete = False)             
        return  querySet

class ColorListView(ListView):
    template_name = "BasicSettings/ColorList.html"
    def get_queryset(self,*args ,**kwargs):
        querySet = ItemColor.objects.filter(IsDelete = False)             
        return  querySet

class SizeListView(ListView):
    template_name = "BasicSettings/SizeList.html"
    def get_queryset(self,*args ,**kwargs):
        querySet = ItemSize.objects.filter(IsDelete = False)             
        return  querySet


