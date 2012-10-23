# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "examenes/about.html"}, name="indice_examenes"),
    url(r"^subir/$", ExamenCreate.as_view(), name="upload_examen"),
    url(r"^lista/$", ExamenList.as_view(), name="lista_examenes"),
)
