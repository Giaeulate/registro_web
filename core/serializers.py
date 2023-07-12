from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *



class MunicipioSerializer(ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class ComunidadSerializer(ModelSerializer):
    class Meta:
        model = Comunidad
        # fields = '__all__'
        fields = ['id', 'name',]


class CustomMunicipioSerializer(ModelSerializer):
    comunidades = ComunidadSerializer(many=True, read_only=True)

    class Meta:
        model = Municipio
        fields = '__all__'

class FormularioEncuestaSerializer(ModelSerializer):
    class Meta:
        model = FormularioEncuesta
        fields = '__all__'

class PhotoPersonSerializer(ModelSerializer):
    class Meta:
        model = PhotoPerson
        fields = '__all__'

class PhotoFormSerializer(ModelSerializer):
    class Meta:
        model = PhotoForm
        fields = '__all__'