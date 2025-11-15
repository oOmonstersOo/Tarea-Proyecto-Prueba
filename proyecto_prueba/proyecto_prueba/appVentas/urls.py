from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("clientes/", views.lista_clientes, name='lista_clientes'),
    path("tiendas/", views.lista_tiendas, name='lista_tiendas'),
    path("compras/", views.lista_compras, name='lista_compras'),
    path("nuevo_cliente/", views.crear_cliente, name="crear_cliente"),
    path("nuevo_tienda/", views.crear_tienda, name='crear_tienda'),
    path("nuevo_compra/", views.crear_compra, name='crear_compra'),
    path("eliminar_cliente/<int:id>/", views.eliminar_cliente, name="eliminar_cliente"),
    path("eliminar_tienda/<int:id>/", views.eliminar_tienda, name="eliminar_tienda"),
    path("eliminar_compra/<int:id>/", views.eliminar_compra, name='eliminar_compra'),
    path("actualizar_cliente/<int:id>/", views.actualizar_cliente, name='actualizar_cliente'),
    path("actualizar_tienda/<int:id>/", views.actualizar_tienda, name="actualizar_tienda"),
    path("actualizar_compra/<int:id>/", views.actualizar_compra, name="actualizar_compra")

]