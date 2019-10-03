from django.contrib import admin
from BasicSettings.models import UomMaster , UomDetails  

# Register your models here.
class UomMasterAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'UomMasterName',
        'UomMasterShortName', 
        'IsActive' ,
        'IsDelete',
        'CreateDate'
        ]
admin.site.register(UomMaster, UomMasterAdmin )
