# -*- coding: utf-8 -*-
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
#from django.core.urlresolvers import resolve
#from django.core.urlresolvers import reverse_lazy
from models import Examen
from forms import *

class ExamenCreate(CreateView):
    model = Examen
    form_class = ExamenForm
    ##Sacamos la dirección del equipo cliente y la pasamos como initial_data para el form
    def get_initial(self):
        super(ExamenCreate, self).get_initial()
        return {"equipo": "%s"%(self.request.META["REMOTE_ADDR"])}

class ExamenUpdate(UpdateView):
    model = Examen

class ExamenDelete(DeleteView):
    model = Examen
    #success_url = reverse_lazy('examenes')

class ExamenList(ListView):
    model = Examen
    queryset = Examen.objects.all().order_by('curso','fecha_subida')
