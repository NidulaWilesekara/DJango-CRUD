from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def index(request):
    student_to_update = None
    if request.method == "POST":
        student_id = request.POST.get("id")
        name = request.POST["name"]
        email = request.POST["email"]
        age = request.POST["age"]

        if student_id:  # UPDATE
            student = Student.objects.get(pk=student_id)
            student.name = name
            student.email = email
            student.age = age
            student.save()
        else:  # CREATE
            Student.objects.create(name=name, email=email, age=age)

        return redirect("/")

    # GET request
    edit_id = request.GET.get("edit")
    if edit_id:
        student_to_update = get_object_or_404(Student, pk=edit_id)

    students = Student.objects.all()
    return render(request, "crudapp/index.html", {"students": students, "student_to_update": student_to_update})


def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect("/")
