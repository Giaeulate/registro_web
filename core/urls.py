from django.urls import path
from .views import *


urlpatterns = [
    path('municipio/', MunicipioList.as_view(), name='municipio-list-page'),
    path('municipio/<slug:pk>/', MunicipioDetail.as_view(), name='municipio-detail-page'),
    path('comunidad/', ComunidadList.as_view(), name='comunidad-list-page'),
    path('comunidad/<slug:pk>/', ComunidadDetail.as_view(), name='comunidad-detail-page'),

    path('custom_municipio/', CustomMunicipioList.as_view(), name='custom_municipio-list-page'),
    path('custom_municipio/<slug:pk>/', CustomMunicipioDetail.as_view(), name='custom_municipio-detail-page'),

    path('formulario_encuesta/', FormularioEncuestaList.as_view(), name='formulario_encuesta-list-page'),
    path('formulario_encuesta/<slug:pk>/', FormularioEncuestaDetail.as_view(), name='formulario_encuesta-detail-page'),
    path('photo_person/', PhotoPersonList.as_view(), name='photo_person-list-page'),
    path('photo_person/<slug:pk>/', PhotoPersonDetail.as_view(), name='photo_person-detail-page'),
    path('photo_form/', PhotoFormList.as_view(), name='photo_form-list-page'),
    path('photo_form/<slug:pk>/', PhotoFormDetail.as_view(), name='photo_form-detail-page'),

    path('create_form/', CreateForm.as_view(), name='create-form'),
    path('create_form_estructure/', CreateFormEstructure.as_view(), name='create-form-estructure'),
]