from django.contrib import admin
from slatino.apps.Publications.models import Publication, PublicationDescription, PublicationPhoto
from django.conf import settings


class PublicationInlineDescription(admin.StackedInline):
    model = PublicationDescription
    max_num = len(settings.LANGUAGES)
    extra = len(settings.LANGUAGES)

    fields = ('lang', 'title', 'description', 'published')


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'pub_date', 'post_type', 'published')
    prepopulated_fields = {"slug": ("name", )}

    inlines = [PublicationInlineDescription, ]

    class Media:
        js = (settings.MEDIA_URL + 'tiny_mce/tiny_mce.js',
              settings.MEDIA_URL + 'Publication-media/dcarticletextarea.js',
              )


class PublicationPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication', 'stamp')


admin.site.register(PublicationPhoto, PublicationPhotoAdmin)
admin.site.register(Publication, PublicationAdmin)
