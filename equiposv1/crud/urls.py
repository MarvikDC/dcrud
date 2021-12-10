from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("", views.home, name="home"),
    path("", views.welcome, name="bienvenido"),
    path("main", views.home, name="home"),
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:equipo_id>/", views.eliminar, name="eliminar"),
    path("editar/<int:equipo_id>/", views.editar, name="editar"),
    path("ayuda/", views.helpdesk, name="ayuda"),
    path("archivos/", views.uploadFile, name = "uploadFiles"),
    path("archivosprivados/", views.privateFile, name = "privateFiles"),
    path("detallearchivo/<int:archivo_id>/", views.detallefile, name="detallearchivo"),
    path("listas/", views.equipos, name="listas"),
]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
    