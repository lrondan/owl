from django.db import models


class QuoteRequest(models.Model):

    SERVICE_CHOICES = (
        ('Black', 'Black Box'),
        ('Gray', 'Gray Box'),
        ('White', 'White Box'),
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    company = models.CharField(max_length=100, blank=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.company} - {self.message}"
    

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="Para URLs amigables si lo necesitas")
    descripcion_corta = models.TextField(max_length=300)  # Lo que se muestra en la tarjeta
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('PENTEST', 'Pentesting'),
            ('HARDENING', 'Hardening de Sistemas'),
            ('AUDITORIA', 'Auditoría de Cumplimiento'),
            ('SOC', 'Implementación SOC Básico'),
            ('OTROS', 'Otros Servicios'),
        ],
        default='PENTEST'
    )
    fecha_publicacion = models.DateField()
    url_blog = models.URLField(max_length=500, verbose_name="Enlace al artículo en WordPress")  # ¡Aquí va la clave!
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)  # Opcional: portada
    destacado = models.BooleanField(default=False)  # Para filtrar los más importantes

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_publicacion']


