from  django import forms
from .models import *

from django.forms  import ModelForm  #for model form use

import json
from django.forms import ModelChoiceField

class UomMasterForm(ModelForm):

    class Meta:
        model = UomMaster
        fields = ['UomMasterName','UomMasterShortName','IsActive' ]
        labels = {
            'UomMasterName': "UOM Master Name:",
            'UomMasterShortName': "UOM Short Name:",
            'IsActive': "Active :"
        }
        widgets = {
            'UomMasterName': forms.TextInput(),
            'UomMasterShortName': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),
        }

    def __init__(self,*args, **kwargs):
        self.postData = None
        self.instance = None

        
        super(UomMasterForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
        if(len(args) > 0):
            self.postData =  args[0]
        
        self.fields['UomMasterName'].widget.attrs['class']="form-control masterName"
        self.fields['UomMasterShortName'].widget.attrs['class']="form-control mseterShortName"
        
        if self.instance is not None and self.postData is None :
            self.fields['UomMasterName'].initial = self.instance.UomMasterName
            self.fields['UomMasterShortName'].initial = self.instance.UomMasterShortName
            self.fields['IsActive'].initial = self.instance.IsActive
            
 
    def clean(self):

        # super(UomMasterForm, self).__init__(*args, **kwargs)
        
        data = self.cleaned_data
        name = self.cleaned_data.get("UomMasterName")
        shortName = self.cleaned_data.get("UomMasterShortName")
        self.fields['UomMasterName'].widget.attrs['class']="form-control masterName"
        self.fields['UomMasterShortName'].widget.attrs['class']="form-control mseterShortName"
        if name is None or name=="" :
           raise forms.ValidationError('UOM Master Name Required')
        elif shortName is None or shortName=="" :
            raise forms.ValidationError('Short Name  Required')
        else:
            return data
    

    def clean_UomMasterName(self):
        name = self.cleaned_data.get("UomMasterName")
        queryet = UomMaster.objects.filter(UomMasterName=name)
        if queryet.exists():
            print(queryet)
            raise  forms.ValidationError("UOM Already Exists")
        return name

class UomDetailsForm(ModelForm):
   

        
    def __init__(self,*args, **kwargs):
        
        self.postData = None
        self.instance = None
        
        
        super(UomDetailsForm, self).__init__(*args, **kwargs)
        
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
        if(len(args) > 0):
            self.postData =  args[0]
           
        
        self.fields['UomDetailsName'].widget.attrs['class']="form-control name"
        self.fields['UomDetailsShortName'].widget.attrs['class']="form-control shortName"
        self.fields['ConversionValue'].widget.attrs['class']="form-control conversionValue"

            


        if self.instance is not None and self.postData is None :
            self.fields['UomDetailsName'].initial = self.instance.UomDetailsName
            self.fields['UomDetailsShortName'].initial = self.instance.UomDetailsShortName
            self.fields['ConversionValue'].initial = self.instance.ConversionValue
            

        if self.postData is not None :
           
            theTr = self.postData.get('trCount')
            if (theTr is not None):
                self.fields['UomDetailsName'].widget.attrs['id'] = str(theTr)+'_'+'UomDetailsName'
                self.fields['UomDetailsShortName'].widget.attrs['id'] = str(theTr)+'_'+'UomDetailsShortName'
                self.fields['ConversionValue'].widget.attrs['id'] = str(theTr)+'_'+'ConversionValue'
                self.fields['EqualToMaster'].widget.attrs['id'] = str(theTr)+'_'+'EqualToMaster'

            self.fields['UomDetailsName'].initial = self.postData.get('UomDetailsName')
            self.fields['UomDetailsShortName'].initial = self.postData.get('UomDetailsShortName')
            self.fields['ConversionValue'].initial = self.postData.get('ConversionValue')
            self.fields['EqualToMaster'].initial = self.postData.get('EqualToMaster')
            

        
    
    def clean(self,*args, **kwargs):
        
        super(UomDetailsForm, self).clean() 
        data = self.cleaned_data
        name = self.cleaned_data.get("UomDetailsName")
        short = self.cleaned_data.get("UomDetailsShortName")
        conversion = self.cleaned_data.get("ConversionValue")
 
        if name is None or name=="" :
           raise forms.ValidationError('UOM Details Name Required')
        elif short is None or short=="" :
            raise forms.ValidationError('UOM Details Short Name Required')
        elif conversion is None or short==0 :
            raise forms.ValidationError('Valid Conversion Value Required')
        
        else:
            return data
   


    class Meta:
        model = UomDetails
        exclude = ('UomMaster',)
        fields = ['UomDetailsName', 'UomDetailsShortName', 'ConversionValue','EqualToMaster']
        labels = {
            'UomDetailsName': "Details Name:",
            'UomDetailsShortName': "Short Name:",
            'ConversionValue': "Conversion Value :",
            'EqualToMaster': "Equal to Master:",
        }
        widgets= {
            'UomDetailsName': forms.TextInput(), 
            'UomDetailsShortName': forms.TextInput(), 
            'ConversionValue': forms.NumberInput(), 
            'EqualToMaster': forms.CheckboxInput(), 
        }

class UomMasterEditForm(ModelForm):

    class Meta:
        model = UomMaster
        
        fields = [  'UomMasterName','UomMasterShortName','IsActive' ]
        labels = {
            'UomMasterName': "UOM Master Name:",
            'UomMasterShortName': "UOM Short Name:",
            'IsActive': "Active :"
        }
        widgets = {
            
            'UomMasterName': forms.TextInput(),
            'tada': forms.TextInput(),
            'UomMasterShortName': forms.TextInput(),
            'IsActive': forms.CheckboxInput(),
        }
        

    def __init__(self,*args, **kwargs ):
        
        
        self.postData = None
        self.instance = None

        
        super(UomMasterEditForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
        if(len(args) > 0):
            self.postData =  args[0]
 
        self.fields['UomMasterName'].widget.attrs['class']="form-control masterName"
        self.fields['UomMasterShortName'].widget.attrs['class']="form-control mseterShortName"
        
        if self.instance is not None and self.postData is None :
            self.fields['UomMasterName'].initial = self.instance.UomMasterName

            self.fields['UomMasterShortName'].initial = self.instance.UomMasterShortName
            self.fields['IsActive'].initial =self.instance.IsActive
        if self.postData is not None:
            self.fields['UomMasterName'].initial = self.postData.get('UomMasterName') 
            self.fields['UomMasterShortName'].initial = self.postData.get('UomMasterShortName') 
            self.fields['IsActive'].initial =self.postData.get('IsActive') 


    def clean(self):
        data = self.cleaned_data
        name = self.cleaned_data.get("UomMasterName")
        short = self.cleaned_data.get("UomMasterShortName")
        if name is None or name=="" :
           raise forms.ValidationError('UOM Master Name Required')
        elif short is None or short=="" :
            raise forms.ValidationError('UOM  Short Name Required') 
        else:
            return data
    def clean_UomMasterName(self):

        name = self.cleaned_data.get("UomMasterName")
        id = self.instance.pk
        querySet = UomMaster.objects.filter(UomMasterName =name and id != id )
        
        if(querySet.count()>0):
            raise  forms.ValidationError("UOM Already Exists")
        return name


class ItemGroupForm(ModelForm):

    def __init__(self, *args , **kwargs ):

        self.postData = None
        self.instance = None
        super(ItemGroupForm, self).__init__(*args, **kwargs)

        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
        if(len(args) > 0):
            self.postData =  args[0]

        self.fields['ItemGroupName'].widget.attrs['class']="form-control masterName"
        self.fields['GroupShortName'].widget.attrs['class']="form-control shortName"
        
        if self.instance is not None and self.postData is None :
            self.fields['ItemGroupName'].initial = self.instance.ItemGroupName
            self.fields['GroupShortName'].initial = self.instance.GroupShortName
            self.fields['IsActive'].initial =self.instance.IsActive

        if self.postData is not None :
            self.fields['ItemGroupName'].initial = self.postData.get('ItemGroupName')
            self.fields['GroupShortName'].initial = self.postData.get('GroupShortName')
            self.fields['IsActive'].initial =self.postData.get('IsActive')
    def clean(self):
        data = self.cleaned_data
        name = self.cleaned_data.get("ItemGroupName")
        if name is None or name=='':
            raise forms.ValidationError("Group Name Required")
        return data
    
    def clean_ItemGroupName(self):

        name = self.cleaned_data.get("ItemGroupName")
        groupId = self.instance.pk
        querySet = ItemGroup.objects.exclude(id=groupId).filter(ItemGroupName =name  )
        
        if(querySet.count()>0):
            raise  forms.ValidationError("Name Already Exists")
        return name
    
    def clean_GroupShortName(self):

        name = self.cleaned_data.get("GroupShortName")
        groupId = self.instance.pk
        querySet = ItemGroup.objects.exclude(id=groupId).filter(GroupShortName =name)
        
        if(name==None or name==''):
            raise  forms.ValidationError("Short Name Required")
        if(querySet.count()>0):
            raise  forms.ValidationError("Name Already Exists")
        if len(name)>3:
            raise  forms.ValidationError("Short Name Max Length 3")
        return name


    class Meta:
        model = ItemGroup
        fields = ['ItemGroupName','GroupShortName','IsActive' ]
        labels = {
            'ItemGroupName': "Group Name:",
            'GroupShortName': "Short Name",
            'IsActive': "Active :"
        }
        widgets = {
            'ItemGroupName': forms.TextInput(),
            'GroupShortName': forms.TextInput(),
            
            'IsActive': forms.CheckboxInput(),
        }

#region ItemCategotyForm


class ItemCategoryForm(ModelForm):
    #creator_choices = [(c.id, c.ItemGroA:upName) for c in ItemGroup.objects.all()]
    
    class Meta:
        
        model = ItemCategory
        fields = ['ItemGroup','ItemCategory', 'CategoryShortName','IsActive',  ]
        
        
    def __init__(self, *args, **kwargs):


        self.postData = None
        self.instance = None
        super(ItemCategoryForm, self).__init__(*args, **kwargs)


        self.fields['ItemGroup'].widget.attrs['class']="form-control masterName"
        self.fields['ItemCategory'].widget.attrs['class']="form-control"
        self.fields['CategoryShortName'].widget.attrs['class']="form-control"
        self.fields['ItemGroup'].queryset  =  ItemGroup.objects.filter(IsActive=1)
        self.fields['ItemGroup'].empty_label  =  'Select Group'
        self.fields['ItemGroup'].initial  = '0'
        
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
            #self.instance.pk = self.postData.get('id')
        if(len(args) > 0):
            self.postData =  args[0]
        
        if self.instance is not None:
            self.fields['ItemGroup'].queryset  =  ItemGroup.objects.filter(IsActive=1)
            self.fields['ItemCategory'].initial = self.instance.ItemCategory
            self.fields['CategoryShortName'].initial =self.instance.CategoryShortName
            self.fields['IsActive'].initial =self.instance.IsActive
            
        if self.postData is not None :
            self.fields['ItemGroup'].queryset  =  ItemGroup.objects.filter(IsActive=1)
            self.fields['ItemCategory'].initial = self.postData.get('ItemCategory')
            self.fields['CategoryShortName'].initial = self.postData.get('CategoryShortName')
            self.fields['IsActive'].initial =self.postData.get('IsActive')

        
    

    def clean_ItemGroup(self):
        group = self.cleaned_data.get("ItemGroup")
        if group is None or group=='' :
            raise  forms.ValidationError("Group Selection Required")
        return group
    
        
    def clean_ItemCategory(self):
        group = self.cleaned_data.get("ItemGroup")
        
        name = self.cleaned_data.get("ItemCategory")
        catId = self.instance.pk
        qs = ItemCategory.objects.exclude(id=catId).filter(ItemGroup_id = group.pk , ItemCategory = name  )
        
        if(name is None or name==""):
            raise  forms.ValidationError("Category Name Required")
        if(qs.count()>0):
            raise  forms.ValidationError("Category Name Already Exists")
        return name
    
    def clean_CategoryShortName(self):
        group = self.cleaned_data.get("ItemGroup")
        name = self.cleaned_data.get("CategoryShortName")
        catId = self.instance.pk
        
        qs = ItemCategory.objects.exclude(id=catId).filter( CategoryShortName = name , ItemGroup_id=group.pk)
        if(name is None or name==""):
            raise  forms.ValidationError("Short Name Required")
        if(qs.count()>0):
            raise  forms.ValidationError("Short Name Already Exists In Same Group")
        return name
    
    def clean(self):
        data = self.cleaned_data
        group = self.cleaned_data.get("ItemGroup")
        name = self.cleaned_data.get("ItemCategory")
        short = self.cleaned_data.get("CategoryShortName")
        
        if(short is None or short==""):
            raise  forms.ValidationError("Short Name Required")
        if(name is None or name==""):
            raise  forms.ValidationError("Category Name Required")
        if(group is None or group=="0" or group==0):
            raise  forms.ValidationError("Group Selection Required")
        return data
        
#endregion

#region ItemBrand
class ItemBrandForm(ModelForm):
    class Meta:
        
        model = ItemBrand
        fields = ['ItemBrandName','IsActive']

    def __init__(self, *args, **kwargs):


        self.postData = None
        self.instance = None
        super(ItemBrandForm, self).__init__(*args, **kwargs)
        self.fields['ItemBrandName'].widget.attrs['class']="form-control masterName"
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
            #self.instance.pk = self.postData.get('id')
        if(len(args) > 0):
            self.postData =  args[0]       
        if self.instance is not None:
            
            self.fields['ItemBrandName'].initial = self.instance.ItemBrandName
            
            self.fields['IsActive'].initial =self.instance.IsActive
            
        if self.postData is not None :
            
            self.fields['ItemBrandName'].initial = self.postData.get('ItemBrandName')
           
            self.fields['IsActive'].initial =self.postData.get('IsActive')

    def clean(self):
        data = self.cleaned_data
        brandName = self.cleaned_data.get("ItemBrandName")
        
        
        if(brandName is None or brandName==""):
            raise  forms.ValidationError("Brand Name Required")
        
        return data

    def clean_ItemBrandName(self):
        name = self.cleaned_data.get("ItemBrandName")
        brandId = self.instance.pk
        querySet = ItemBrand.objects.exclude(id=brandId).filter(ItemBrandName =name)
        
        if(name==None or name==''):
            raise  forms.ValidationError("Brand Name Required")
        if(querySet.count()>0):
            raise  forms.ValidationError("Name Already Exists")
        
        return name

#endregion

#regiom Item Color

class ItemColorForm(ModelForm):
    class Meta:
        
        model = ItemColor
        fields = ['ItemColorName','IsActive']

    def __init__(self, *args, **kwargs):


        self.postData = None
        self.instance = None
        super(ItemColorForm, self).__init__(*args, **kwargs)
        self.fields['ItemColorName'].widget.attrs['class']="form-control masterName"
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
            
        if(len(args) > 0):
            self.postData =  args[0]       
        if self.instance is not None:
            
            self.fields['ItemColorName'].initial = self.instance.ItemColorName
            
            self.fields['IsActive'].initial =self.instance.IsActive
            
        if self.postData is not None :
            
            self.fields['ItemColorName'].initial = self.postData.get('ItemColorName')
           
            self.fields['IsActive'].initial =self.postData.get('IsActive')

    def clean(self):
        data = self.cleaned_data
        colorName = self.cleaned_data.get("ItemColorName")
        
        
        if(colorName is None or colorName==""):
            raise  forms.ValidationError("Color Name Required")
        
        return data

    def clean_ItemColorName(self):
        name = self.cleaned_data.get("ItemColorName")
        colorId = self.instance.pk
        querySet = ItemColor.objects.exclude(id=colorId).filter(ItemColorName =name)
        
        if(name==None or name==''):
            raise  forms.ValidationError("Color Name Required")
        if(querySet.count()>0):
            raise  forms.ValidationError("Color Already Exists")
        
        return name


#endregion


#regiom Item Size

class ItemSizeForm(ModelForm):
    class Meta:
        
        model = ItemSize
        fields = ['ItemSizeName','IsActive']

    def __init__(self, *args, **kwargs):


        self.postData = None
        self.instance = None
        super(ItemSizeForm, self).__init__(*args, **kwargs)
        self.fields['ItemSizeName'].widget.attrs['class']="form-control masterName"
        if 'instance' in kwargs:
            self.instance =  kwargs.pop("instance" or None)
            
        if(len(args) > 0):
            self.postData =  args[0]       
        if self.instance is not None:
            
            self.fields['ItemSizeName'].initial = self.instance.ItemSizeName
            
            self.fields['IsActive'].initial =self.instance.IsActive
            
        if self.postData is not None :
            
            self.fields['ItemSizeName'].initial = self.postData.get('ItemSizeName')
           
            self.fields['IsActive'].initial =self.postData.get('IsActive')

    def clean(self):
        data = self.cleaned_data
        sizeName = self.cleaned_data.get("ItemSizeName")
        
        
        if(sizeName is None or sizeName==""):
            raise  forms.ValidationError("Color Name Required")
        
        return data

    def clean_ItemSizeName(self):
        name = self.cleaned_data.get("ItemSizeName")
        sizeId = self.instance.pk
        querySet = ItemSize.objects.exclude(id=sizeId).filter(ItemSizeName =name)
        
        if(name==None or name==''):
            raise  forms.ValidationError("Size Name Required")
        if(querySet.count()>0):
            raise  forms.ValidationError("Size Already Exists")
        
        return name


#endregion
    


        

    
    
  


        
    




        
    

    


     
    


