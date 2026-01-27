from django.contrib import admin
from .models import Employee
# Register your models here.
# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_name','emp_email','emp_sal','emp_depart']
    