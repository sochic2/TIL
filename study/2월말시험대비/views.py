from django.shortcuts import render, redirect
from .models import Student

def index(request):
    students = Student.objects.all()
    # students = Student.objects.order_by('-id')

    return render(request, 'students/index.html', {'students' : students})

def create(request):
    name = request.GET.get('name')
    e-mail = request.GET.get('e-mail')
    # name = request.POST.get('name')
    student = Student(name=name, e-mail=e-mail)
    student.save()
    return redirect('/students/')

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')



from .models import Student
def index(request):
    students = Student.objects.all()
    # students = Student.objects.oreder_by('-id')
    return render(request, 'students/index.html', {'students':students})

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'detail.html', {'student':student})

def create(request):
    name = request.GET.get('name')
    e-mail = request.GET.get('e-mail')

    student = Student(name=name, e-mail=e-mail)
    return redirect('/students/')

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')


def index(request):
    students = Student.objects.all()
    return render(request 'students/index.html',{'students':students})