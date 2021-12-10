from django.urls import path
from django.urls.conf import include
from . import views

from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path("", views.index, name="index"),
    #path("logear/", views.logear, name="logear"),
    path("crearusuario/", views.crearusuario, name="crearusuario"),
    path('accounts/', include('django.contrib.auth.urls')),

    
]