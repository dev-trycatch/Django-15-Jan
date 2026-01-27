from django.shortcuts import render,redirect
from .models import Employee
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        e_name = request.POST.get('emp_name')
        e_email = request.POST.get('emp_email')
        e_sal = request.POST.get('emp_sal')
        e_depart = request.POST.get('emp_depart')

        Employee.objects.create(
            emp_name = e_name,
            emp_email = e_email,
            emp_sal = e_sal,
            emp_depart = e_depart,
        )
        messages.success(request,'Employee created successfully!!!')
        return redirect('/home')
    queryset = Employee.objects.all()
    context = {
        'data':queryset
    }
    return render(request,'index.html',context)

def update_emp(request,id):
    queryset = Employee.objects.get(id = id)

    if request.method == 'POST':
        e_name = request.POST.get('emp_name')
        e_email = request.POST.get('emp_email')
        e_sal = request.POST.get('emp_sal')
        e_depart = request.POST.get('emp_depart')

        queryset.emp_name = e_name
        queryset.emp_email = e_email
        queryset.emp_sal = e_sal
        queryset.emp_depart = e_depart
        queryset.save()
        messages.success(request,'Employee updated successfully!!!')
        return redirect('/home')

    context = {
        'data':queryset
    }
    return render(request,'update.html',context)

def delete_emp(request,id):
    queryset = Employee.objects.get(id = id)
    queryset.delete()
    messages.success(request,'Employee Deleted successfully!!!')
    return redirect('/home')