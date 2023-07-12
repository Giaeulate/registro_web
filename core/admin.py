from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin, ImportExportModelAdmin
from django.utils.html import format_html

@admin.register(Municipio)
class MunicipioAdmin(ImportExportModelAdmin):
    list_display = [x.name for x in Municipio._meta.fields]
    # search_fields = ['',]

@admin.register(Comunidad)
class ComunidadAdmin(ImportExportModelAdmin):
    list_display = [x.name for x in Comunidad._meta.fields]
    # search_fields = ['',]


@admin.register(FormularioEncuesta)
class FormularioEncuestaAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'ci', 'latitude', 'longitude', 'photo_ci_front_url', 'photo_ci_back_url']
    # list_display_links = ['id', 'photo_ci_front', 'photo_ci_back']

    def photo_ci_front_url(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.photo_ci_front)
    photo_ci_front_url.short_description = 'PHOTO CI FRONTAL'
    photo_ci_front_url.allow_tags = True

    def photo_ci_back_url(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.photo_ci_back)
    photo_ci_back_url.short_description = 'PHOTO CI REVERSO'
    photo_ci_back_url.allow_tags = True


@admin.register(PhotoPerson)
class PhotoPersonAdmin(ImportExportModelAdmin):
    list_display = ['id', 'url_data']

    def url_data(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.url)
    url_data.short_description = 'URL'
    url_data.allow_tags = True

@admin.register(PhotoForm)
class PhotoFormAdmin(ImportExportModelAdmin):
    list_display = ['id', 'url_data']

    def url_data(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.url)
    url_data.short_description = 'URL'
    url_data.allow_tags = True

@admin.register(FormularioPiquete)
class FormularioPiqueteAdmin(ImportExportModelAdmin):
    list_display = [x.name for x in FormularioPiquete._meta.fields]
    # search_fields = ['',]

@admin.register(PhotoCampo)
class PhotoCampoAdmin(ImportExportModelAdmin):
    list_display = ['id', 'url_data']

    def url_data(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.url)
    url_data.short_description = 'URL'
    url_data.allow_tags = True

@admin.register(PhotoEstructura)
class PhotoEstructuraAdmin(ImportExportModelAdmin):
    list_display = ['id', 'url_data']

    def url_data(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.url)
    url_data.short_description = 'URL'
    url_data.allow_tags = True