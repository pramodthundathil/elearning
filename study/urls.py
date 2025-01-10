from django.urls import path
from .import views

urlpatterns = [ 
    path("course",views.course,name="course"),
    path("add_study_materials",views.add_study_materials,name="add_study_materials"),
    path("study_materials_list",views.study_materials_list,name="study_materials_list"),
    path("study_materials_detail/<int:pk>",views.study_materials_detail,name="study_materials_detail"),
    path("edit_study_materials/<int:pk>",views.edit_study_materials,name="edit_study_materials"),
    path("study_materials_admin",views.study_materials_admin,name="study_materials_admin"),
    path("update_material_admin/<int:pk>",views.update_material_admin,name="update_material_admin"),
    path("approve_verification/<int:pk>",views.approve_verification,name="approve_verification"),
    path("course_delete/<int:pk>",views.course_delete,name="course_delete"),

    # courses 
    path("my_course",views.my_course,name="my_course"),
    path("course_edit/<int:pk>",views.course_edit,name="course_edit"),
    path("add_classes/<int:pk>",views.add_classes, name="add_classes"),
    path("course_details/<int:pk>",views.course_details,name="course_details")

]