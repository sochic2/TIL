from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.order_by('-id')
    return render(request, 'students/index.html', {'students':students})
    
def new(request):
    return render(request, 'students/new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    
    student = Student(name=name, email=email, birthday=birthday, age=age)
    student.save()
    return redirect('/students/')

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')
    
def edit(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/edit.html', {'student' : student})
    
def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    student.save()
    return redirect('/students/')
