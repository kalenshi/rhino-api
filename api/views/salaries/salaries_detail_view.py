from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Salaries
from api.views.salaries.serializers import SalariesSerializer
from pagination.salary_pagination import SalaryPagination


class SalariesDetailView(APIView):
    """
    Class to interact with the salaries model
    """
    serializer_class = SalariesSerializer
    pagination_class = SalaryPagination

    def get(self, request, emp_no, format=None):
        """
        Retrieve the current salary
        :param request:
        :param format:
        :return:
        """
        query_set = Salaries.objects.filter(emp_no=emp_no)
        pagination = self.pagination_class()
        paginated_result = pagination.paginate_queryset(query_set, request)

        serializer = self.serializer_class(paginated_result, many=True)

        return pagination.get_paginated_response(
            data=serializer.data
        )

    def post(self, request):
        """
        create an employees salary
        :param request:
        :return:
        """
        return Response({"message": "coming soon"})
