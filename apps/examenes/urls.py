# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required, permission_required
from views import *

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "examenes/about.html"}, name="indice_examenes"),
    url(r"^subir/$", ExamenCreate.as_view(), name="upload_examen"),
    url(r"^lista/$", login_required(ExamenList.as_view()), name="lista_examenes"),
)
