from django.shortcuts import render
from django.urls import reverse_lazy

from .models import AnimalModel, ShelterModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import AnimalCreateForm


class AnimalListView(ListView):
    model = AnimalModel
    template_name = 'animals/list.html'
    context_object_name = 'animal_list'

    def get_queryset(self):
        return AnimalModel.objects.all()


class AnimalCreateView(CreateView):
    form_class = AnimalCreateForm
    template_name = 'animals/create.html'
    context_object_name = 'animal_create'
    success_url = reverse_lazy('animal_list')