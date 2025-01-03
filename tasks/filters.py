import django_filters
from .models import Task

# Filtro de tarefas.
class TaskFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by name')
    date = django_filters.DateFilter(lookup_expr='exact', label='Filter by date')
    is_completed = django_filters.BooleanFilter(label='Filter by completion status')

    class Meta:
        model = Task
        fields = ['name', 'date', 'is_completed']