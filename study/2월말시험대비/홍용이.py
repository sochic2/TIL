from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students':students})

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'detail.html', {'student':student})

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect(index)