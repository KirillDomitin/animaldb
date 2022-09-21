from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import AnimalModel, ShelterModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, RedirectView
from .forms import AnimalCreateForm


class AnimalListView(ListView):
    model = AnimalModel
    template_name = 'animals/animal_list.html'
    context_object_name = 'animal_list'

    def get_queryset(self):
        return AnimalModel.objects.order_by('pk').all()


class AnimalCreateView(CreateView):
    form_class = AnimalCreateForm
    template_name = 'animals/animal_create.html'
    context_object_name = 'animal_create'
    success_url = reverse_lazy('animal_list')


class AnimalUpdateView(UpdateView):
    model = AnimalModel
    template_name = 'animals/animal_update.html'
    context_object_name = 'animal_update'
    fields = '__all__'
    success_url = reverse_lazy('animal_list')

class AnimalDeleteView(DeleteView):
    model = AnimalModel
    template_name = 'animals/animal_delete.html'
    context_object_name = 'animal_delete'
    success_url = reverse_lazy('animal_list')

class AnimalDetailView(DetailView):
    model = AnimalModel
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal_detail'
