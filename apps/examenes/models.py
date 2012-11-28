# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
import os
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
    """Ajustamos el nombre dle fichero a guardar para que contenga la clase y el nombre del alumno"""
    #print "tenemos la instance:", instance
    #print "Y el fichero:",filename
    path = "ficheros_examenes"
    format = instance.curso + "_" + slugify(instance.nombre) + "_" + filename
    return os.path.join(path, format)

class Examen(models.Model):
    nombre = models.CharField(max_length=255)
    equipo = models.CharField(max_length=255)
    fecha_subida = models.DateField(auto_now_add=True)
    fichero =  models.FileField(upload_to=ajustar_nombre_fichero)
    curso = models.CharField(max_length=2, choices=CURSOS)
    evaluacion = models.DecimalField( max_digits=2, decimal_places=0, choices=EVALUACION)
    def evaluacion_nombre(self):
        return EVALUACION[int(self.evaluacion)][1]
    def get_absolute_url(self):
        return "/examenes"
