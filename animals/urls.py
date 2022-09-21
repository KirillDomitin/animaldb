from django.urls import path
from .views import AnimalListView, AnimalCreateView, AnimalUpdateView, AnimalDeleteView, AnimalDetailView

urlpatterns = [
    path('', AnimalListView.as_view(), name='animal_list'),
    path('create/', AnimalCreateView.as_view(), name='animal_create'),
    path('<int:pk>/update/', AnimalUpdateView.as_view(), name='animal_update'),
    path('<int:pk>/delete/', AnimalDeleteView.as_view(), name='animal_delete'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='animal_detail'),
]