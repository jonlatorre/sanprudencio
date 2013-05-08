# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
import os
from django.utils.translation import gettext_lazy as _

# Create your models here.

CURSOS = (
    ('1A', '1º A'),
    ('1B', '1º B'),
    ('2A', '2º A'),
    ('2B', '2º B'),
    ('3A', '3º A'),
    ('3B', '3º B'),
    ('4A', '4º A'),
    ('4B', '4º B'),
    ('TI', 'TIC'),
    ('DA', 'DAO'),
)
EVALUACION = (
    ( 0, "1ªEval"),
    ( 1, "2ªEval"),
    ( 2, "3ªEval"),
    ( 3, "Ordinaria"),
    ( 4, "Extraordinaria"),
)

def ajustar_nombre_fichero(instance, filename):
    """Ajustamos el nombre del fichero a guardar para que contenga la clase y el nombre del alumno"""
    #print "tenemos la instance:", instance
    #print "Y el fichero:",filename
    path = "ficheros_examenes"
    #FIXME esto lo debería calcular
    ano = "2012_13"
    curso = slugify(instance.curso)
    #FIXME hay que sacar el nombre de la evalución no el número
    evaluacion = slugify(instance.get_evaluacion_display())
    format = slugify(instance.nombre) + "_" + filename
    print "Vamos a guardarlo en ..:"
    print path, ano, curso, evaluacion, format
    return os.path.join(path, ano, curso, evaluacion, format)

class Examen(models.Model):
    nombre = models.CharField(_('Nombre y Apellidos'),max_length=255,)
    equipo = models.CharField(max_length=255)
    fecha_subida = models.DateField(auto_now_add=True)
    fichero =  models.FileField(_('Fichero del examen'),upload_to=ajustar_nombre_fichero)
    curso = models.CharField(max_length=2, choices=CURSOS)
    evaluacion = models.DecimalField( max_digits=2, decimal_places=0, choices=EVALUACION)
    def evaluacion_nombre(self):
        return EVALUACION[int(self.evaluacion)][1]
    def get_absolute_url(self):
        #return "/examenes"
        return reverse("indice_examenes")
    def __str__(self):
        return "%s-%s-%s"%(self.curso,self.evaluacion,self.nombre)
    def __unicode__(self):
        return "%s-%s-%s"%(self.curso,self.evaluacion,self.nombre)
