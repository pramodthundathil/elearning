from django.shortcuts import render, redirect
from .forms import UserAddForm, StudentForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import admin_only, unauthenticated_user, allowed_users, student_user_check
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.

# Create your views here.
@admin_only
@student_user_check
def HomePage(request):
    return render(request,"index.html")


@login_required(login_url="SignIn")
def AdminIndex(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='staff')
            user.groups.add(group) 
            messages.success(request,"User Registration Successful")
            return redirect("AdminIndex")
        else:
            messages.error(request,"Something went Wrong!!! Try To use password Includes (UPPERCASE, Numbers, Sepecial Characters and Minimum Legth 8  Characters) or User or email id Already Exists")
            return redirect("AdminIndex")
    context = {
        "form":form,
        
    }
    return render(request,"adminindex.html",context)

@unauthenticated_user
def SignIn(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST["pswd"]
        user = authenticate(request,username= uname, password = password)
        if user is not None:
            login(request,user)
            return redirect('HomePage')
        else:
            messages.info(request,"Username or Password Incorrect")
            return redirect('SignIn')
    return render(request,"login.html")

@unauthenticated_user
def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful")
            return redirect("SignIn")
        else:
            messages.error(request,form.errors)
            return redirect("SignUp")
    
    context = {"form":form}
    return render(request,"register.html",context)


def SignOut(request):
    logout(request)
    return redirect("SignIn")

def user_type_confirmation(request):
    return render(request,"user_type_confirmation.html")

@login_required(login_url="SignIn")
def student_confirm(request):
    user = request.user 
    group = Group.objects.get(name="student")
    user.groups.add(group)
    user.save()
    if Student.objects.filter(user=user).exists():
        return redirect('HomePage')
    else:
        return redirect('register_student')

@login_required(login_url="SignIn")    
def register_student(request):
    form = StudentForm()
    if request.method == "POST":    
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.student_id = request.user.id
            student.save()
            messages.success(request,"Student Registration Successful")
            return redirect('HomePage')
        else:
            messages.error(request,"Something went Wrong!!!")
            return redirect('register_student')
    context = {"form":form}
    return render(request,"register_student.html", context) 


@login_required(login_url="SignIn")
def teacher_confirm(request):
    user = request.user 
    group = Group.objects.get(name="teacher")
    user.groups.add(group)
    user.save()
    return redirect('HomePage')


def teacher_index(request):
    return render(request,"teacher_index.html")


@login_required(login_url="SignIn")
def student_details(request):
    students = User.objects.filter(groups__name='student')
    context = {"students": students}
    return render(request, "student_details.html", context)


@login_required(login_url="SignIn")
def teacher_details(request):
    teachers = User.objects.filter(groups__name='teacher')
    context = {"teachers": teachers}
    return render(request, "teacher_details.html", context)



@login_required(login_url="SignIn")
def add_student(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request, "Student added successfully")
            return redirect("AdminIndex")
        else:
            messages.error(request, "Error adding student")
            return redirect("add_student")
    context = {"form": form}
    return render(request, "add_student.html", context)

def delete_student(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, "Student deleted successfully")
    return redirect("student_details")

@login_required(login_url="SignIn")
def add_teacher(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='teacher')
            user.groups.add(group)
            messages.success(request, "Teacher added successfully")
            return redirect("AdminIndex")
        else:
            messages.error(request, "Error adding teacher")
            return redirect("add_teacher")
    context = {"form": form}
    return render(request, "add_teacher.html", context)

@login_required(login_url="SignIn")
def update_student(request, student_id):
    user = User.objects.get(id=student_id)
    form2 = StudentForm(instance=user.student)
    form = UserUpdateForm(instance=user)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("AdminIndex")
        else:
            messages.error(request, "Error updating student")
            return redirect("update_student", student_id=student_id)
    context = {"form": form,"form2":form2}
    return render(request, "update_student.html", context)


@login_required(login_url="SignIn")
def update_teacher(request, teacher_id):
    user = User.objects.get(id=teacher_id)
    form = UserAddForm(instance=user)
    if request.method == "POST":
        form = UserAddForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher updated successfully")
            return redirect("AdminIndex")
        else:
            messages.error(request, "Error updating teacher")
            return redirect("update_teacher", teacher_id=teacher_id)
    context = {"form": form}
    return render(request, "update_teacher.html", context)


def verified_users(request,pk):
    users = User.objects.get(id = pk)
    users.student.verified = True
    users.student.save()
    messages.success(request, "User Verified Successfully")
    return redirect("student_details")