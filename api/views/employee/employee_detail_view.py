from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Employees
from api.views.employee.serializers import EmployeeSerializer


class EmployeeDetailView(APIView):
    """
    Class for interacting with the employee model
    """

    serializer_class = EmployeeSerializer

    def get_object(self, emp_no):
        """
        Retrieve an employee using emp_no
        :param emp_no:
        :return:
        """
        return get_object_or_404(Employees, pk=emp_no)

    def get(self, request, emp_no, format=None):
        """
        Retrieve a single employee based on the employee number
        :param request:
        :param format:
        :return:
        """
        employee = self.get_object(emp_no)

        serializer = self.serializer_class(instance=employee)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, emp_no):
        """
        Delete an employee from the database
        :param request:
        :param emp_no:
        :return:
        """
        employee = self.get_object(emp_no)
        serializer = self.serializer_class(instance=employee)
        # employee.delete()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
