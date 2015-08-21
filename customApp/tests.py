from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from mezzanine.pages import views
from customApp.models import DownloadedPage


class DownloadedPageTests(TestCase):

    client = Client()

    #TODO ������-�� ���� ��������, � ������ ������� � �����-�� ������ ���������
    def netest_for_downloaded_data(self):
        for dpage in DownloadedPage.objects.all():
            response = self.client.get(reverse(views.page), kwargs={'slug', dpage.slug})
            self.assertEqual(response.status_code, 200)