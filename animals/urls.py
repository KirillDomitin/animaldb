from django.urls import path
from .views import AnimalListView, AnimalCreateView

urlpatterns = [
    path('', AnimalListView.as_view(), name='animal_list'),
    path('create/', AnimalCreateView.as_view(), name='animal_create'),
]