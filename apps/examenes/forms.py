# -*- coding: utf-8 -*-
from django import forms

from models import Examen

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        template = "examenes/examen_form.html"
        exclude = ('equipo',)
    def save(self, *args, **kwargs):
        cliente = "%s - %s"%(self.request.META["REMOTE_HOST"].self.request.META["REMOTE_ADDR"])
        print cliente
        self.equipo = cliente
        super(ExamenForm, self).save(*args, **kwargs)
