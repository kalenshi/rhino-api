from django.db import models

from api.models.employees import Employees


class Titles(models.Model):
    emp_no = models.OneToOneField(Employees, models.DO_NOTHING, db_column="emp_no", primary_key=True)
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "titles"
        unique_together = (("emp_no", "title", "from_date"),)
