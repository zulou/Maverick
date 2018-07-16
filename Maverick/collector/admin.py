from django.contrib import admin
from . import models

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    search_fields = ['id','firstname','lastname','dni','cellphone','email']
    list_display = ('id','firstname','lastname','dni','cellphone','email')

admin.site.register(models.clients,ClientsAdmin)
