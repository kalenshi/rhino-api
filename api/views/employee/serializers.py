from rest_framework import serializers

from api.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Class for serializing/deserializing the employee model
    """

    class Meta:
        model = Employees
        fields = (
            "emp_no",
            "birth_date",
            "first_name",
            "last_name",
            "gender",
            "hire_date"
        )
