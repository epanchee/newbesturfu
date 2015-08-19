from django.db import models
from django.http import Http404
from mezzanine.pages.models import Page
import urllib


class DownloadedPage(Page):
    dlink = models.TextField("dlink")

    def download(self):
        f = urllib.urlopen(self.dlink)
        try:
            response = f.read()
            if f.getcode() == 404:
                raise Http404("Page doesn't exist")
        except:
            response = "Something wrong. Can't load data from given link."
        return response.decode('cp1251')