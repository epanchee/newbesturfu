from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import DownloadedPage


admin.site.register(DownloadedPage, PageAdmin)
