from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Titulo", max_length=100, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(
        verbose_name="Data de Entrega", null=False, blank=False
    )
    finish_at = models.DateTimeField(null=True)
