from django.db import models

from api.models.employees import Employees


class Salaries(models.Model):
    emp_no = models.OneToOneField(Employees, models.DO_NOTHING, db_column="emp_no", primary_key=True)
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = "salaries"
        unique_together = (("emp_no", "from_date"),)

    def __str__(self):
        """
        String representation of the Salaries model
        :return:
        """
        return f"{self.emp_no}: {self.from_date}"
