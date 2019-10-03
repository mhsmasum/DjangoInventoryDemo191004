from django.shortcuts import render
from .forms import ProductForm
from BasicSettings.models import *
from ProductSetup.models import *
import json
from django.http import JsonResponse , HttpResponse
from ProductSetup.ProductHelper import ProductHelper
from Utility.ResultResponse import ResultResponse
from Utility.AppError import AppError
from django.template.loader import render_to_string

# Create your views here.

_aProductHelper =  ProductHelper()
def Index(request):
    return render(request, 'ProductSetup/index.html', {})



def NewProduct(request):
    masterForm = ProductForm( None)
    context = {
        'masterForm':masterForm,
        
    }
    return render(request, 'ProductSetup/NewProduct.html', context)

def SaveProduct(request):
    aResponse = ResultResponse()
    received_json_data = json.loads(request.body.decode("utf-8"))
    theRequest = request.POST.copy()
    theRequest.__mutable = True
    theRequest.POST=received_json_data
    
    name = received_json_data.get('ProductName')
    description = received_json_data.get('ProductDescripTion')
    country = received_json_data.get('ProductCountry')
    category = received_json_data.get('ProductCategory')
    brand = received_json_data.get('ProductBrand')
    color = received_json_data.get('ProductColor')
    size = received_json_data.get('ProductSize')
    uom = received_json_data.get('ProductUOM')

    masterForm = ProductForm(theRequest.POST)

    if masterForm.is_valid():
        productGenerate = _aProductHelper.GenerateProduct(name ,description,category,country,brand,uom,color,size)
        finalProd = productGenerate[0]
        productColor = productGenerate[1]
        productsize = productGenerate[2]
        # need to add trunsection process
        finalProd.save()

        if productColor is not None:
            finalProd.ProductColor.add(*productColor)
        if productsize is not None:
            finalProd.ProductSize.add(*productsize)
        
        finalProd.ProductCode = _aProductHelper.GenerateProductCode(category = category , productid =finalProd.pk )
        finalProd.save()
        if finalProd.pk>0:
            aResponse.IsSuccess = True
        return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    else:
        appError = AppError()
        template = render_to_string('ProductSetup/_productForm.html' , {'masterForm':masterForm  } )
        appError.TheData = str(template)
        return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)

    # productGenerate = _aProductHelper.GenerateProduct(name ,description,category,country,brand,uom,color,size)
    
    # finalProd = productGenerate[0]
    # productColor = productGenerate[1]
    # productsize = productGenerate[2]

    # need to add trunsection process
    # finalProd.save()

    # if productColor is not None:
    #     finalProd.ProductColor.add(*productColor)
    # if productsize is not None:
    #     finalProd.ProductSize.add(*productsize)
    
    # finalProd.ProductCode = _aProductHelper.GenerateProductCode(category = category , productid =finalProd.pk )
    # finalProd.save()
    # if finalProd.pk>0 :
    #     aResponse.IsSuccess = True
    #     return JsonResponse(json.dumps(aResponse.__dict__ ), safe=False)
    # else:
    #     appError = AppError()

    #     template = render_to_string('ProductSetup/NewProduct.html' , {'masterForm':masterForm  } )
    #     appError.TheData = str(template)
    #     return JsonResponse( json.dumps(appError.__dict__ ) , safe=False)

    

    


    
