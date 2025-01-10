from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StudyMaterials, Classes_for_Course, Courses
from .forms import StudyMaterialsForm, CoursesForm, ClassesForCourseForm


def course(request):
    courses = Courses.objects.all()
    context = {
        "courses":courses
    }
    return render(request, "course.html",context )


def course_details(request, pk):
    course = Courses.objects.get(id = pk)
    return render(request,"course_details.html",{"course":course})

@login_required(login_url="SignIn")
def add_study_materials(request):
    form = StudyMaterialsForm() 
    materials  = StudyMaterials.objects.filter(user=request.user)
    if request.method == "POST":
        form = StudyMaterialsForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit= False)
            material.user = request.user
            material.save()
            messages.success(request, "Study Materials Added Successfully")
            return redirect("add_study_materials")
        else:
            messages.error(request, "Something went Wrong!!!")
            return redirect("add_study_materials")
        
    context = {"form": form, "materials": materials}    
    return render(request, "add_study_materials.html",context)

def edit_study_materials(request, pk):
    material = get_object_or_404(StudyMaterials, pk=pk)
    form = StudyMaterialsForm(instance=material)
    if request.method == "POST":
        form = StudyMaterialsForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, "Study Materials Updated Successfully")
            return redirect("add_study_materials")
        else:
            messages.error(request, "Something went Wrong!!!")
            return redirect("add_study_materials")
    return render(request, "edit_study_materials.html", {"form": form})


def study_materials_list(request):
    materials = StudyMaterials.objects.all()
    context = {"materials": materials}
    return render(request, "study_materials.html", context)


def study_materials_detail(request, pk):
    material = get_object_or_404(StudyMaterials, pk=pk)
    context = {"material": material}
    return render(request, "study_materials_detail.html", context)


# adminfunctions = [add_study_materials, edit_study_materials, study_materials_list, study_materials_detail]

# for func in adminfunctions:

def study_materials_admin(request):
    materials = StudyMaterials.objects.all()

    context = {"materials": materials}
    return render(request, "study_materials_admin.html", context)


def update_material_admin(request,pk):
    materials = get_object_or_404(StudyMaterials, pk=pk)
    form = StudyMaterialsForm(instance=materials)
    context = {"form": form,"materials":materials}
    return render(request, "update_material_admin.html",context)

def approve_verification(request,pk):
    materials = get_object_or_404(StudyMaterials, pk=pk)
    materials.verified = True
    materials.save()
    messages.success(request, "Study Materials Updated Successfully")
    return redirect("study_materials_admin")

def delete_material_admin(request,pk):
    materials = get_object_or_404(StudyMaterials, pk=pk)
    materials.delete()
    messages.success(request, "Study Materials Deleted Successfully")
    return redirect("study_materials_admin")




# courses teacher 

def my_course(request):
    form = CoursesForm()
    course = Courses.objects.filter(user = request.user)

    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            courses = form.save(commit=False)
            courses.user = request.user
            courses.save()
            messages.success(request,"course added......")
            return redirect("my_course")

    context = {
        "form":form,
        "course":course
    }
    return render(request,"teacher/my-course.html",context)


def course_delete(request,pk):
    course = get_object_or_404(Courses, id = pk)
    course.delete()
    messages.success(request,"course added......")
    return redirect(my_course)


def course_edit(request,pk):
    course = get_object_or_404(Courses, id = pk)
    form = CoursesForm(instance=course)
    form1 = ClassesForCourseForm()
    if request.method == "POST":
        form = CoursesForm(request.POST,instance=course)
        if form.is_valid():
            courses =  form.save()
            courses.save()
            messages.info(request,"course updated......")
            return redirect("my_course")
        else:
            messages.info(request,"course updated error......")
            return redirect("my_course")

    context = {
        "form":form,
        "form1":form1,
        "course":course
    }
    return render(request,'teacher/course_update.html',context)


def add_classes(request, pk):
    courses = get_object_or_404(Courses, id = pk)
    if request.method == "POST":
        form = ClassesForCourseForm(request.POST,request.FILES )
        if form.is_valid():
            classes = form.save(commit=False)
            classes.course = courses
            classes.save()
            return redirect(course_edit, pk = pk)
