from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import DownloadedPage, Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('partners_name', 'logo_url',)


admin.site.register(Partner, PartnerAdmin)
admin.site.register(DownloadedPage, PageAdmin)
