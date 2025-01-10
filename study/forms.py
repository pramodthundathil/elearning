from django import forms
from .models import StudyMaterials

class StudyMaterialsForm(forms.ModelForm):
    class Meta:
        model = StudyMaterials
        fields = ['title',"course","stream", 'category', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'stream': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import Courses, Classes_for_Course

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [ 'course_title', 'description']
        widgets = {
            'course_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ClassesForCourseForm(forms.ModelForm):
    class Meta:
        model = Classes_for_Course
        fields = [ 'title', 'description', 'video', 'material']
        widgets = {
            
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'material': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
