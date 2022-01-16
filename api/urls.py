from django.urls import path

from api.views.employee.employee_detail_view import EmployeeDetailView
from api.views.employee.employee_list_view import EmployeeListView
from api.views.salaries.salaries_detail_view import SalariesDetailView

app_name = "api"

urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/<emp_no>/", EmployeeDetailView.as_view(), name="employee-details"),
    path("salary/<emp_no>/", SalariesDetailView.as_view(), name="employee-salaries"),
]
