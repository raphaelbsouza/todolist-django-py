from django.db import models
from datetime import date


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Titulo", max_length=30, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(
        verbose_name="Data de Entrega", null=False, blank=False
    )
    finish_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_completed(self):
        if not self.finish_at:
            self.finish_at = date.today()
            self.save()
