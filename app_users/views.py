from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView

import animals
from .forms import UserRegistrationForm, AuthForm, ProfileUpdateForm
from .models import Profile


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            password=form.cleaned_data.get('password1'))
            Profile.objects.create(user=user, shelter=form.cleaned_data.get('shelter'))
            group = Group.objects.filter(name='ShelterGroup').first()
            if group:
                group.user_set.add(user)
                group.save()
            else:
                group = Group.objects.create(name='ShelterGroup')
                group.user_set.add(user)
                group.save()
            perm = Permission.objects.filter(content_type__model='animalmodel').all()
            print(perm)
            # perm_list = ['animals.add_animalmodel',
            #              'animals.change_animalmodel',
            #              'animals.view_animalmodel',
            #              'animals.delete_animalmodel']
            group.permissions.set(perm)
            group.save()
            login(request, user)
            return redirect('animal_list')
        print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'app_users/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect('animal_list')
            form.add_error('__all__', 'Проверьте правильность написания логина и пароля!')
    else:
        form = AuthForm()
    return render(request, 'app_users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('animal_list')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'app_users/profile_detail.html'
    context_object_name = 'detail'

    def get_object(self, queryset=None):
        obj = Profile.objects.filter(id=self.kwargs['pk']).select_related('user').first()
        return obj

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data()
        if self.request.user.profile.pk == context['object'].pk:
            context['is_owner'] = True
        else:
            context['is_owner'] = False
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'app_users/profile_update.html'
    context_object_name = 'profile_update'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data()
        if self.request.user.profile.pk == context['object'].pk:
            context['is_owner'] = True
        else:
            context['is_owner'] = False
        return context
