# -*- coding: utf-8 -*-
from django import forms

from models import Examen

class ExamenForm(forms.ModelForm):

    class Meta:
        model = Examen
        template = "examenes/examen_form.html"
        #Escondemos el input del nombre de equipo
        widgets = {
            'equipo': forms.HiddenInput()
        }
