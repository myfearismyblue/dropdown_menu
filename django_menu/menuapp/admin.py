from django.contrib import admin

# Register your models here.
from menuapp.models import MenuNode, Menu

admin.site.register(Menu)
admin.site.register(MenuNode)
