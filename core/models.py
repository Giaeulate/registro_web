from django.db.models import *


class URLFieldExtended(URLField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 500
        super().__init__(*args, **kwargs)

class Municipio(Model):
    id = CharField(primary_key=True, max_length=255)
    name = CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f"{self.name}"


class Comunidad(Model):
    id = CharField(primary_key=True, max_length=255)
    name = CharField(max_length=255, verbose_name='Nombre')
    municipio = ForeignKey(Municipio, on_delete=CASCADE, related_name='comunidades')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Comunidad'
        verbose_name_plural = 'Comunidades'

    def __str__(self):
        return f"{self.name}"
    
    
class FormularioEncuesta(Model):
    id = CharField(primary_key=True, max_length=255)
    comunidad = ForeignKey(Comunidad, on_delete=CASCADE)
    name = CharField(max_length=255)
    ci = CharField(max_length=255)
    latitude = FloatField()
    longitude = FloatField()
    photo_ci_front = URLFieldExtended(blank=True, null=True)
    photo_ci_back = URLFieldExtended(blank=True, null=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulario Encuesta'
        verbose_name_plural = 'Formularios Encuesta'

    def __str__(self):
        return f"{self.name}"
    

class PhotoPerson(Model):
    id = CharField(primary_key=True, max_length=255)
    url = URLFieldExtended(blank=True, null=True)
    form = ForeignKey(FormularioEncuesta, on_delete=CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Photo Persona'
        verbose_name_plural = 'Photos Persona'

    def __str__(self):
        return f"{self.url}"
    

class PhotoForm(Model):
    id = CharField(primary_key=True, max_length=255)
    url = URLFieldExtended(blank=True, null=True)
    form = ForeignKey(FormularioEncuesta, on_delete=CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Photo Encuesta'
        verbose_name_plural = 'Photos Encuestas'

    def __str__(self):
        return f"{self.url}"
    


class FormularioPiquete(Model):
    id = CharField(primary_key=True, max_length=255)
    comunidad = ForeignKey(Comunidad, on_delete=CASCADE)
    name = CharField(max_length=255)
    latitude = FloatField()
    longitude = FloatField()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulario Piquete'
        verbose_name_plural = 'Formularios Piquete'

    def __str__(self):
        return f"{self.name}"

class PhotoCampo(Model):
    id = CharField(primary_key=True, max_length=255)
    url = URLFieldExtended(blank=True, null=True)
    form = ForeignKey(FormularioPiquete, on_delete=CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Photo Campo'
        verbose_name_plural = 'Photos Campo'

    def __str__(self):
        return f"{self.url}"
    

class PhotoEstructura(Model):
    id = CharField(primary_key=True, max_length=255)
    url = URLFieldExtended(blank=True, null=True)
    form = ForeignKey(FormularioPiquete, on_delete=CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Photo Estructura'
        verbose_name_plural = 'Photos Estructuras'

    def __str__(self):
        return f"{self.url}"