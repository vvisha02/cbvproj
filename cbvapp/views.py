from django.shortcuts import render
from django.views.generic import CreateView
from .models import Employee

# Create your views here.

class EmployeeCreate(CreateView):
    model=Employee
    template='employee_form.html'
    fields='__all__'

class EmployeeList(ListView):
    model=Employee
    template_name='employee_list.html'
    def get_queryset(self):
        qs=Employee.objects.all()
        template_name='employee_details.html'
