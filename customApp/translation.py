from modeltranslation.translator import TranslationOptions, translator
from customApp.models import DownloadedPage


class DownloadedPageTranslationOptions(TranslationOptions):
    fields = ('dlink',)

translator.register(DownloadedPage, DownloadedPageTranslationOptions)