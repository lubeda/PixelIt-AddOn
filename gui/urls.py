from django.urls import include, path
from . import views

urlpatterns = [
    path('screens/', views.screens, name='all_screens'),
    path('screen/<str:name>/', views.screen, name='one_screen'),
    path('templates/', views.templates, name='all_templates'),
    path('template/<str:name>/', views.template, name='one_template'),
]
