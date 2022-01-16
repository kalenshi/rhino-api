from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Employees
from pagination import EmployeePagination
from api.views.employee.serializers import EmployeeSerializer


class EmployeeListView(APIView):
    """
    Class for interacting with the employee model without an id
    """
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get(self, request, format=None):
        """
        List all the employees
        :param request:
        :return:
        """
        employees = Employees.objects.all()

        pagination = self.pagination_class()

        result = pagination.paginate_queryset(employees, request)
        serializer = self.serializer_class(result, many=True)

        return pagination.get_paginated_response(serializer.data)

    def post(self, request):
        """
        Create an employee and save it in the database
        :param request:
        :return:
        """
        employee_data = request.data

        serializer = self.serializer_class(data=employee_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
