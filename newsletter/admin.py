from django.contrib import admin

from newsletter.models import ServiceClient


# Register your models here.
@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'client_name', 'client_comment')