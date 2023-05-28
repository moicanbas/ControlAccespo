from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MarcacionModel
from django.http import JsonResponse
from django_serverside_datatable_post.views import ServerSideDatatablePostView

#SERVICIOS
class MarcacionEntradaView(TemplateView,LoginRequiredMixin):
    template_name='marcacion/servicio/marcar_entrada.html'

class EntradaSalidaView(View):
    def post(self, request, *args, **kwargs):
        try:
            accion = self.request.POST.get('accion')
            hora = self.request.POST.get('hora')
            fecha = self.request.POST.get('fecha')
            user = self.request.user
            if accion =='entrada':
                MarcacionModel.objects.create(
                    usuario= user,
                    hora_marcacion_entrada= hora,
                    fecha_marcacion_entrada=fecha
                )
            else:
                MarcacionModel.objects.create(
                    usuario= user,
                    hora_marcacion_salida= hora,
                    fecha_marcacion_salida=fecha
                )

            return JsonResponse({"success": True, "msg": 'Marcación almacenada exitosamente'}, status=200)

        except Exception as e:
            print(e)
            return JsonResponse({"success": False, "msg": str(e)}, status=400)

#PROCESOS
class RegistroMarcaciones(TemplateView,LoginRequiredMixin):
    template_name='marcacion/proceso/registro.html'

class EmpleadosListView(ServerSideDatatablePostView):
    columns = ['usuario__identificacion','usuario__first_name',
            'usuario__last_name', 'hora_marcacion_entrada','fecha_marcacion_entrada',
            'hora_marcacion_salida','fecha_marcacion_salida'
    ]

    def get_queryset(self):
        queryset = MarcacionModel.objects.filter(activo=True)
        if not queryset:
            return MarcacionModel.objects.none()
        return queryset

