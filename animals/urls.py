from django.urls import path

from .views import AnimalListView, AnimalCreateView, AnimalUpdateView, AnimalDetailView, delete_view

urlpatterns = [
    path('', AnimalListView.as_view(), name='animal_list'),
    path('create/', AnimalCreateView.as_view(), name='animal_create'),
    path('<int:pk>/update/', AnimalUpdateView.as_view(), name='animal_update'),
    path('<int:pk>/delete/', delete_view, name='animal_delete'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
]