from django.conf import settings
from django.db import models
from django.utils import timezone

# Modelo das tarefas.
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'