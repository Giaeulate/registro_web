from django.shortcuts import render
from core.models import *
from core.serializers import *
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class MunicipioList(ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class MunicipioDetail(RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class ComunidadList(ListCreateAPIView):
    queryset = Comunidad.objects.all()
    serializer_class = ComunidadSerializer

class ComunidadDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comunidad.objects.all()
    serializer_class = ComunidadSerializer

class CustomMunicipioList(ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = CustomMunicipioSerializer

class CustomMunicipioDetail(RetrieveUpdateDestroyAPIView):
    queryset = Municipio.objects.all()
    serializer_class = CustomMunicipioSerializer

class FormularioEncuestaList(ListCreateAPIView):
    queryset = FormularioEncuesta.objects.all()
    serializer_class = FormularioEncuestaSerializer

class FormularioEncuestaDetail(RetrieveUpdateDestroyAPIView):
    queryset = FormularioEncuesta.objects.all()
    serializer_class = FormularioEncuestaSerializer

class PhotoPersonList(ListCreateAPIView):
    queryset = PhotoPerson.objects.all()
    serializer_class = PhotoPersonSerializer

class PhotoPersonDetail(RetrieveUpdateDestroyAPIView):
    queryset = PhotoPerson.objects.all()
    serializer_class = PhotoPersonSerializer

class PhotoFormList(ListCreateAPIView):
    queryset = PhotoForm.objects.all()
    serializer_class = PhotoFormSerializer

class PhotoFormDetail(RetrieveUpdateDestroyAPIView):
    queryset = PhotoForm.objects.all()
    serializer_class = PhotoFormSerializer


class CreateForm(GenericAPIView):
    def post(self, request, format=None):
        try:
            body = request.data
            form = FormularioEncuesta()
            form.id = body["id"]
            form.name = body["name"]
            form.latitude = body["latitude"]
            form.longitude = body["longitude"]
            form.ci = body["ci"]
            form.photo_ci_front = body["photo_ci_front"]["url"]
            form.photo_ci_back = body["photo_ci_back"]["url"]
            form.comunidad = Comunidad.objects.get(pk=body["comunidad"])
            form.save()
            
            for item in body["photos_person"]:
                photoPerson = PhotoPerson()
                photoPerson.id = item["id"]
                photoPerson.url = item["url"]
                photoPerson.form = form
                photoPerson.save()

            for item in body["photos_form"]:
                photoForm = PhotoForm()
                photoForm.id = item["id"]
                photoForm.url = item["url"]
                photoForm.form = form
                photoForm.save()

            return Response({"status": True}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"status": False}, status=HTTP_200_OK)
    
class CreateFormEstructure(GenericAPIView):
    def post(self, request, format=None):
        try:
            body = request.data
            form = FormularioPiquete()
            form.id = body["id"]
            form.name = body["name"]
            form.comunidad = Comunidad.objects.get(pk=body["comunidad"])
            form.latitude = body["latitude"]
            form.longitude = body["longitude"]
            form.save()
            
            for item in body["photos_campo"]:
                photoCampo = PhotoCampo()
                photoCampo.id = item["id"]
                photoCampo.url = item["url"]
                photoCampo.form = form
                photoCampo.save()

            for item in body["photos_estructura"]:
                photoEstructura = PhotoEstructura()
                photoEstructura.id = item["id"]
                photoEstructura.url = item["url"]
                photoEstructura.form = form
                photoEstructura.save()

            return Response({"status": True}, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"status": False}, status=HTTP_200_OK)
 