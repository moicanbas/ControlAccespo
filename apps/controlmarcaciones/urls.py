from django.urls import path
from .views import *

urlpatterns = [
  path('',  MarcacionEntradaView.as_view(), name='home'),
  path('marcar_entrada_salida',EntradaSalidaView.as_view(), name='marcar_entrada_salida'),
  path('administrar', RegistroMarcaciones.as_view(), name='administrar'),
  path('datos_empleados', EmpleadosListView.as_view(), name='datos_empleados'),
]
