from  django import forms
from .models import *
from BasicSettings.models import CountryOrigin 

from django.forms  import ModelForm  

class ProductForm(ModelForm):
    class Meta:
        model = ProductInfo
        fields = [
            'ProductName',
            'ProductDescripTion',
            
            'ProductCountry',
            'ProductCategory',
            'ProductBrand' ,
            'ProductColor',
            'ProductSize',
            'ProductUOM',
            'IsActive' ]
        labels = {
            'ProductName': "Name",
            'ProductDescripTion': "Description",
            
            'ProductCountry':'Origin',
            'ProductCategory': 'Category',
            'ProductBrand':'Brand',
            'ProductColor':'Color',
            'ProductSize': 'Size',
            'ProductUOM': 'UOM',
            'IsActive': "Active :"
        }
        
        widgets = {
            'ProductName': forms.TextInput(),
            'ProductDescripTion': forms.TextInput(),
            
            # 'ProductColor': forms.ModelMultipleChoiceField( queryset = ItemColor.objects.filter(IsActive=True , IsDelete = False )),
            'IsActive': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        self.postData = None
        self.instance = None
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['ProductName'].widget.attrs['class']="form-control"
        self.fields['ProductDescripTion'].widget.attrs['class']="form-control"
       
        self.fields['ProductCategory'].widget.attrs['class']="form-control"
        self.fields['ProductCountry'].widget.attrs['class']="form-control"
        self.fields['ProductBrand'].widget.attrs['class']="form-control"
      
        self.fields['ProductColor'].widget.attrs['class']="form-control"
        self.fields['ProductColor'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['ProductColor'].queryset = ItemColor.objects.filter(IsActive=True , IsDelete = False )
        
        self.fields['ProductSize'].widget.attrs['class']="form-control"
        self.fields['ProductSize'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['ProductSize'].queryset = ItemSize.objects.filter(IsActive=True , IsDelete = False )
        
        self.fields['ProductUOM'].widget.attrs['class']="form-control"
        

        self.fields['ProductCategory'].queryset  = ItemCategory.objects.filter(IsActive=True , IsDelete = False )
        self.fields['ProductCategory'].empty_label  =  'Select Category'
        

        self.fields['ProductCountry'].queryset  = CountryOrigin.objects.filter(IsActive=True , IsDelete = False )
        self.fields['ProductCountry'].empty_label  =  'Select Country'

        self.fields['ProductBrand'].queryset  = ItemBrand.objects.filter(IsActive=True , IsDelete = False )
        self.fields['ProductBrand'].empty_label  =  'Select Brand'

        self.fields['ProductColor'].queryset  = ItemColor.objects.filter(IsActive=True , IsDelete = False )
        

        self.fields['ProductSize'].queryset  = ItemSize.objects.filter(IsActive=True , IsDelete = False )
        


    def clean(self):
        data = self.cleaned_data
        name = self.cleaned_data.get("ProductName")
        desc = self.cleaned_data.get("ProductDescripTion")
        category = self.cleaned_data.get("ProductCategory")
        country = self.cleaned_data.get("ProductCountry")
        brand = self.cleaned_data.get("ProductBrand")
        uomMaster = self.cleaned_data.get("ProductUOM")

        if name is None or '':
            raise forms.ValidationError('Product Name Required')
        elif desc is None or '':
            raise forms.ValidationError('Product Description Required')
        elif category is None or '':
            raise forms.ValidationError('Product Category Required')
        elif country is None or '':
            raise forms.ValidationError('Country Origin Required')
        elif brand is None or '':
            raise forms.ValidationError('Brand Required')
        elif uomMaster is None or '':
            raise forms.ValidationError('UOM Required')
        else:
            return data
        




