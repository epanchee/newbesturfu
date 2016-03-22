from django.db import models
from django.http import Http404
from django.utils.translation import ugettext as _
from mezzanine.pages.models import Page
import urllib


class DownloadedPage(Page):
    dlink = models.TextField(name="dlink", verbose_name=_('Download link'))

    def download(self):
        f = urllib.urlopen(self.dlink)
        try:
            response = f.read()
            if f.getcode() == 404:
                raise Http404("Page doesn't exist")
        except:
            response = "Something wrong. Can't load data from given link."
        return response.decode('cp1251')


class Partner(models.Model):
    logo_url = models.CharField(name="logo_url", verbose_name=_("Partner's logo"), max_length=255)
    partners_name = models.CharField(name="partners_name", verbose_name=_("Partner's name"), max_length=100)
    href = models.CharField(name="href", verbose_name=_("Partner's link to the website"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")
