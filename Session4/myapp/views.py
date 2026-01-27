from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

def home(request):
    # context = {}
    # print(request.POST.get('sname'))
    # print(request.POST.get('sage'))
    # print(request.POST.get('semail'))

    if request.method == 'POST':
        name = request.POST.get('sname')
        age = request.POST.get('sage')
        email = request.POST.get('semail')

        Student.objects.create(
            name = name,
            age = age,
            email = email,
        )
        messages.success(request, "Data save successfully.")
        return redirect('home')

        # context = {
        #     "name":name,
        #     "age":age,
        #     'email':email
        # }
    # return render(request,'index.html',context)
    return render(request,'index.html')


def student_data(request):
    queryset = Student.objects.all()
    context = {
        'data':queryset
    }
    return render(request,'data.html',context)