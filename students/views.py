from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.db.models import Q

def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "create_student.html", {"form": form})

def student_list(request):
    id_query = request.GET.get('id', '')  # Get the search query for ID
    query = request.GET.get('q', '')  # Get the search query for all other fields

    students = Student.objects.filter(
        Q(id=id_query) if id_query else Q(),  # Search by ID if id_query is not empty
        Q(f_name__icontains=query) |  # Search by first name
        Q(l_name__icontains=query) |  # Search by last name
        Q(email__icontains=query) |   # Search by email
        Q(mobile_number__icontains=query)  # Search by mobile number
    )

    return render(request, "student_list.html", {"students": students, "id_query": id_query, "query": query})

def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "update_student.html", {"form": form})

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "delete_student.html", {"student": student})
