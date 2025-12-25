from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('search/', views.search_notes, name='search_notes'),
    path('crash/', views.crash, name='crash'),
    path('login/', views.insecure_login, name='insecure_login'),
]