from BasicSettings.models import *
from ProductSetup.models import *

################   READ FIRST   ###################### 
# Product Code = GroupShortName:CategoryShortName:100000 (FP:CAT:100001)
# Starts wit 10000

##################################################

class ProductHelper:


    def GetProductColorsFromArray(self, colorArray):
        colorString = 'Not Available'
        colorList = []
        colorIntArray = list(map(int,colorArray))
        if  colorIntArray is not None:
            colorsQuerySet = ItemColor.objects.filter(id__in = colorIntArray)
            if colorsQuerySet.count()>0:
                colorString = ''
                colorLoopCount = 1
                for item in colorsQuerySet:
                    colorList.append(item)
                    if colorsQuerySet.count() != colorLoopCount:
                        colorString = colorString+ item.ItemColorName +','
                    else:
                        colorString =colorString+ item.ItemColorName
                    colorLoopCount = colorLoopCount+1

        return colorString,colorList

    def GetProductSizesFromArray(self , sizeArray):
        sizeString = 'Not Available'
        sizeList = []
        sizeIntArray = list(map(int,sizeArray))
        if  sizeIntArray is not None:
            sizeQuerySet = ItemSize.objects.filter(id__in = sizeIntArray)
            if sizeQuerySet.count()>0:
                sizeString = ''
                sizeLoopCount = 1
                for item in sizeQuerySet:
                    sizeList.append(item)
                    if sizeQuerySet.count() != sizeLoopCount:
                        sizeString = sizeString+ item.ItemSizeName +','
                    else:
                        sizeString =sizeString+ item.ItemSizeName
                    sizeLoopCount = sizeLoopCount+1

        return sizeString,sizeList


    def GenerateProduct(self , name,descriotion, category , country , brand, uom, colors, sizes):
        
        productCategory = ItemCategory.objects.get(id= int(category) )
        theCountry = CountryOrigin.objects.get(id=int(country))
        theBrand = ItemBrand.objects.get(id=int(brand))
        productUom = UomMaster.objects.get(id= int(uom))

        colorMethod = self.GetProductColorsFromArray(colors)
        colorString = colorMethod[0]
        colorObjects = None if  colorString=='Not Available'  else colorMethod[1] 
        
        sizeMethod = self.GetProductSizesFromArray(sizes)
        sizeString = sizeMethod[0]
        sizeObjects =  None if  sizeString=='Not Available'  else sizeMethod[1] 


        theSpecific=''
        theSpecific =theSpecific+ 'Name:'+name+'\n'
        theSpecific =theSpecific+ 'Description:'+descriotion+'\n'
        theSpecific =theSpecific+ 'Category:'+productCategory.ItemCategory+'\n'
        theSpecific =theSpecific+ 'Origin:'+theCountry.CountryName+'\n'
        theSpecific =theSpecific+ 'Brand:'+theBrand.ItemBrandName+'\n'
        theSpecific =theSpecific+ 'UOM:'+productUom.UomMasterName+'\n'
        theSpecific =theSpecific+ 'Colors:'+colorString+'\n'
        theSpecific =theSpecific+ 'Sizes:'+sizeString+'\n'
        aProduct = ProductInfo(
            
            ProductName =name,
            ProductDescripTion = descriotion,
            ProductSpecification = theSpecific,
            ProductCountry = theCountry,
            ProductCategory = productCategory,
            ProductBrand = theBrand,
            
            ProductUOM = productUom,
            ProductCode='SampleProduct',
            IsActive = True
            )
        # for item in colorObjects:
        #     aProduct.ProductColor.add(item)
        # aProduct.ProductColor.add(*colorObjects)
        # aProduct.ProductSize.add(*sizeObjects)
        return aProduct,colorObjects,sizeObjects

    def GenerateProductCode(self,category , productid):
        initial = 10000
        theCategory = ItemCategory.objects.get(id = int(category))
        
        theProductCode = theCategory.ItemGroup.GroupShortName+':'+theCategory.CategoryShortName+':'+str(initial+productid)

        return theProductCode






