from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Capa(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(null=True, max_length=100)
    filtrada = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)
    
    def get_absolute_url(self):
        return reverse("capa-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} (filtrada: {self.filtrada})"