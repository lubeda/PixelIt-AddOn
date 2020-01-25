from django.urls import include, path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('screens/', views.screens, name='all_screens'),
    path('screen/<str:name>/', views.screen, name='one_screen'),
    path('templates/', views.templates, name='all_templates'),
    path('template/<str:name>/', views.template, name='one_template'),
    path('bitmap/<str:name>/', views.bitmap, name='one_bitmap'),
    path('bitmaps/', views.bitmaps, name='all_bitmap'),
    path('form/screen/', views.screenformview, name='enter_screen'),
    path('form/timer/', views.timerformview, name='enter_timer'),
    path('form/alarm/', views.alarmformview, name='enter_alarm'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
