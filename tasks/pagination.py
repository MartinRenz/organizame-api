from rest_framework.pagination import PageNumberPagination

# Paginação de tarefas.
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        page = request.query_params.get(self.page_query_param, None)
        page_size = request.query_params.get(self.page_size_query_param, None)

        if not page and not page_size:
            return None

        return super().paginate_queryset(queryset, request, view)
