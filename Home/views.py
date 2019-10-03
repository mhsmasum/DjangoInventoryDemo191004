from django.shortcuts import render
from MenuSetup.models import *
# Create your views here.

def Index(request):

    appMenu = AppMenu.objects.filter(IsActive=True,IsDelete=False)
    # context = {
    #     'menuItem' : 'Lol'
    # }
    return render(request , 'BasicSettings/homeView.html',{})

def MenuGeneration(context):
    con = context
    path = str(con.path)
    appMenu = AppMenu.GetMenuStepOne(path)
                
    asd2 = list(appMenu[0].MenuStepTwoList)
    
    return {'appMenu' : appMenu , 'path':path}




