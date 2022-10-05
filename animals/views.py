from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .forms import AnimalCreateForm
from .models import AnimalModel


def redirect_main(request):
    return redirect('animal_list', permanent=True)


class AnimalListView(ListView):
    """Список всех животных"""
    model = AnimalModel
    template_name = 'animals/animal_list.html'
    context_object_name = 'animal_list'

    def get_queryset(self):
        # Приюты могут видеть только своих животных, а гости могут видеть всех
        if self.request.user.is_anonymous:
            return AnimalModel.objects.filter(is_deleted=False).order_by('pk').all()
        return AnimalModel.objects.filter(shelter=self.request.user.profile.shelter,
                                          is_deleted=False).order_by('pk').all()


class AnimalCreateView(PermissionRequiredMixin, CreateView):
    """Создание животного"""
    form_class = AnimalCreateForm
    template_name = 'animals/animal_create.html'
    context_object_name = 'animal_create'
    success_url = reverse_lazy('animal_list')
    permission_required = 'animals.add_animalmodel'

    def form_valid(self, form):
        # Тут происходит присваивание животного приюту который его создал
        fields = form.save(commit=False)
        fields.shelter = self.request.user.profile.shelter
        fields.save()
        return super().form_valid(form)


class AnimalUpdateView(PermissionRequiredMixin, UpdateView):
    """Редактирование животного"""
    model = AnimalModel
    template_name = 'animals/animal_update.html'
    context_object_name = 'animal_update'
    fields = ('nickname', 'age', 'weight', 'height', 'identifying_mark', 'shelter')
    success_url = reverse_lazy('animal_list')
    permission_required = 'animals.change_animalmodel'


class AnimalDeleteView(PermissionRequiredMixin, DeleteView):
    """Ужалеине животного из БД (по умолчанию отключено)"""
    model = AnimalModel
    template_name = 'animals/animal_delete.html'
    context_object_name = 'animal_delete'
    success_url = reverse_lazy('animal_list')
    permission_required = 'animals.delete_animalmodel'


class AnimalDetailView(DetailView):
    """Детальная информация по животному"""
    model = AnimalModel
    template_name = 'animals/animal_detail.html'
    context_object_name = 'animal_detail'


@login_required
@permission_required('animals.delete_animalmodel', raise_exception=True)
def delete_view(request, pk):
    """Функция 'мягкого' удаления (установленна по умолчанию)"""
    AnimalModel.objects.filter(pk=pk).first().save_delete()
    return redirect('animal_list')
