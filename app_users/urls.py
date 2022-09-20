from django.urls import path
from .views import registration_view, login_view, logout_view, ProfileDetailView, ProfileUpdateView


urlpatterns = [
    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('<int:pk>/update', ProfileUpdateView.as_view(), name='profile_update')
]