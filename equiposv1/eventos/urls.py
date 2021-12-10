from django.urls import path
from django.urls.conf import include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("", views.index, name="index"),
    #path("logear/", views.logear, name="logear"),
    #path("crearusuario/", views.crearusuario, name="crearusuario"),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('eventos/', views.homeeventos, name="homeeventos"),
    path('leventos/', views.listaeventos, name="temp"),

    
]