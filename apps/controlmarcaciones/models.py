from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    activo = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        default_permissions = ()
        abstract = True

    @classmethod
    def default_queryset(cls):
        return cls.objects.filter(activo=True)
    
class MarcacionModel(BaseModel):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    hora_marcacion_entrada = models.TimeField(null=True, blank=True)
    hora_marcacion_salida = models.TimeField(null=True, blank=True)
    fecha_marcacion_entrada = models.DateField(null=True, blank=True)
    fecha_marcacion_salida = models.DateField(null=True, blank=True)
    

