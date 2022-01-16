from django.db import models


class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1)
    hire_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "employees"

    def __str__(self):
        """
        String representation of the employee model
        :return:
        """
        return f"{self.emp_no}"
