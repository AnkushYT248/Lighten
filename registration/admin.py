from django.contrib import admin
from .models import CustomModel #, Cloth


class CustomModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','image', 'date_created')
    search_fields = ('name', 'email')

    class Media:
        css = {
            'all': ('/static/css/dashboard.css',),
        }

admin.site.register(CustomModel, CustomModelAdmin)

#admin.site.register(Cloth)