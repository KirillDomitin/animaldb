from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import AnimalModel, ShelterModel
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, RedirectView
from .forms import AnimalCreateForm


def redirect_main(request):
    return redirect('animal_list', permanent=True)


class AnimalListView(ListView):
    model = AnimalModel
    template_name = 'animals/animal_list.html'
    context_object_name = 'animal_list'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return AnimalModel.objects.filter(is_deleted=False).order_by('pk').all()
        return AnimalModel.objects.filter(shelter=self.request.user.profile.shelter,
                                          is_deleted=False).order_by('pk').all()


class AnimalCreateView(PermissionRequiredMixin, CreateView):
    form_class = AnimalCreateForm
    template_name = 'animals/animal_create.html'
    context_object_name = 'animal_create'
    success_url = reverse_lazy('animal_list')
    permission_required = 'animals.add_animalmodel'

    def form_valid(self, form):
        print(self.request.user.profile.shelter)
        form.shelter = self.request.user.profile.shelter
        # form.save()
        return super().form_valid(form)


class AnimalUpdateView(PermissionRequiredMixin, UpdateView):
    model = AnimalModel
    template_name = 'animals/animal_update.html'
    context_object_name = 'animal_update'
    fields = ('nickname', 'age', 'weight', 'height', 'identifying_mark', 'shelter')
    success_url = reverse_lazy('animal_list')
    permission_required = 'animals.change_animalmodel'


class AnimalDeleteView(PermissionRequiredMixin, DeleteView):
    model = AnimalModel
    template_name = 'animals/animal_delete.html'
    context_object_name = 'animal_delete'
    success_url = reverse_lazy('animal_list')
    permission_required = 'animals.delete_animalmodel'


class AnimalDetailView(DetailView):
    model = AnimalModel
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal_detail'


@login_required
@permission_required('animals.delete_animalmodel', raise_exception=True)
def delete_view(request, pk):
    AnimalModel.objects.filter(pk=pk).first().save_delete()
    return redirect('animal_list')
