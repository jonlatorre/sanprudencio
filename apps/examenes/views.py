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
    #template = "examenes/examen_form.html"
    #form_class = ExamenForm
    #success_url=resolve('examenes')
    def form_valid(self, form):
        form.instance.request = self.request
        return super(ExamenCreate, self).form_valid(form)

class ExamenUpdate(UpdateView):
    model = Examen

class ExamenDelete(DeleteView):
    model = Examen
    #success_url = reverse_lazy('examenes')

class ExamenList(ListView):
    model = Examen
