from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm


def student_create(request):
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student_list/')
    else:
        form = StudentForm()
    return render(request,'student_create.html', {'form':form})


def student_list(request):
    students =Student.objects.all()
    return render(request,'student_list.html', {'students':students})


def student_edit(request,pk):
    student = get_object_or_404(Student,pk = pk)

    if request.method == "POST":
        form = StudentForm(request.POST,instance= student)
        if form.is_valid():
            form.save()
            return redirect('/student_list/')
    else:
        form = StudentForm(instance= student)
    return render(request,'student_create.html', {'form':form})