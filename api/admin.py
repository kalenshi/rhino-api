from django.contrib import admin

from api.models.employees import Employees
from api.models.titles import Titles
from api.models.department_employee import DeptEmp
from api.models.department_manager import DeptManager
from api.models.salaries import Salaries

# Register your models here.
admin.site.register(Employees)

