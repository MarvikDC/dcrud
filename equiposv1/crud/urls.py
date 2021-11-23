from django.urls import path
from . import views

urlpatterns = [
    #path("", views.home, name="home"),
    path("", views.home, name="home"),
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:equipo_id>/", views.eliminar, name="eliminar"),
    path("editar/<int:equipo_id>/", views.editar, name="editar"),
    path("ayuda/", views.helpdesk, name="ayuda"),
]
