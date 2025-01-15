from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logowanie/', auth_views.LoginView.as_view(template_name='folder_aplikacji/logowanie.html'), name='logowanie'),
    path('accounts/', include('django.contrib.auth.urls')),
]