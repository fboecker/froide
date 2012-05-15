from django.contrib import admin
from django.utils.translation import ugettext as _

from froide.foiidea.models import Source, Article


class SourceAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ['public_bodies', 'foirequests']

admin.site.register(Source, SourceAdmin)
admin.site.register(Article, ArticleAdmin)