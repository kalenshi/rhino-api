from django.db import models

from api.models.departments import Departments


class DeptManager(models.Model):
    emp_no = models.OneToOneField("Employees", models.DO_NOTHING, db_column="emp_no", primary_key=True)
    dept_no = models.ForeignKey(Departments, models.DO_NOTHING, db_column="dept_no")
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = "dept_manager"
        unique_together = (("emp_no", "dept_no"),)
