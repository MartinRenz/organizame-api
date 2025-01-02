from django.db import models
from django.contrib.auth import get_user_model

# Modelo das tarefas.
class Task(models.Model):
    name = models.CharField(max_length=255)
    
    description = models.TextField()
    
    date = models.DateField()
    
    is_completed = models.BooleanField(default=False)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tasks'