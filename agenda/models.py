from django.db import models

# Create your models here.

CONFIANZA = (
    ('A', "ALTA"),
    ('M', "MEDIA"),
    ('B', "BAJA")
)


class Colores(models.Model):
    color = models.CharField(max_length=20)
    descripcion = models.TextField()
    rgb = models.TextField(max_length=12)

    def __unicode__(self):
        return self.color


class Grupos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __unicode__(self):
        return self.nombre


class Contactos(models.Model):
    grupo = models.ForeignKey(Grupos)
    nombre = models.CharField(max_length=100, verbose_name='nombre del compa')
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=250)
    de_confianza = models.BooleanField(default=False)
    colores_favoritos = models.ManyToManyField(Colores)
    confianza = models.CharField(choices=CONFIANZA, max_length=1)

    def __unicode__(self):
        return self.nombre
