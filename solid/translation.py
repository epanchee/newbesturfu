from mezzanine.blog.models import BlogPost
from modeltranslation.translator import TranslationOptions, translator


class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "content",)

translator.register(BlogPost, BlogPostTranslationOptions)