from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput, ModelForm
from .models import Student, MessageStudent
from django import forms
from django.contrib.auth.hashers import make_password




class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
        
        widgets = {
            "first_name":TextInput(attrs={"class":"form-control border-0 py-3","placeholder":"First Name"}),
            "username":TextInput(attrs={"class":"form-control border-0 py-3","placeholder":"Username"}), 
            "email":TextInput(attrs={"class":"form-control border-0 py-3","placeholder":"Email Id"}),    
        }  
        
    def __init__(self, *args, **kwargs):
        super(UserAddForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Password confirmation'})

class UserUpdateForm(UserChangeForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput, help_text="Leave blank if not changing.")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.password = make_password(password)
        if commit:
            user.save()
        return user

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [  'course', 'stream', 'student_roll', 'student_dob']
        widgets = {
            
            
            'course': forms.Select(attrs={'class': 'form-control', 'id': 'course'}),
            'stream': forms.Select(attrs={'class': 'form-control', 'id': 'stream'}),
            'student_roll': forms.TextInput(attrs={'class': 'form-control', 'id': 'student_roll'}),
            'student_dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'student_dob', 'type': 'date'}),
        }

class MessageForm(ModelForm):
    class Meta:
        model = MessageStudent
        fields = ["content"]

        widgets = {
            
            
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'content'}),
            
            
        }
