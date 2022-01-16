from rest_framework.pagination import PageNumberPagination


class SalaryPagination(PageNumberPagination):
    """
    Class to paginate salary response
    """
    page_size = 10
    page_query_param = "s"
    page_size_query_param = "page_size"
