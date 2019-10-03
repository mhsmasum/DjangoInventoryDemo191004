from django.contrib import admin
from .models import MenuStep,MenuType,AppMenu
admin.site.register(
    [MenuStep,MenuType,AppMenu]
    )


# Register your models here.
