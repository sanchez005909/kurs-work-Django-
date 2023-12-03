from django.contrib import admin

from newsletter.models import ServiceClient, Mailing


# Register your models here.
@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'client_name', 'client_comment')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('subject_letter', 'start_time', 'end_time', 'period', 'status',)
