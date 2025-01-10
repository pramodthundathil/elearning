from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='student')
    student_id = models.CharField(max_length=100)
    course = models.CharField(max_length=100, choices=(('B.Tech', 'B.Tech'), 
                                                       ('M.Tech', 'M.Tech'),
                                                        ('MCA', 'MCA'),
                                                        ("BCA","BCA"),
                                                          ('MBA', 'MBA'), 
                                                          ('BBA', 'BBA'), 
                                                        ('B.Sc', 'B.Sc'),
                                                                ('M.Sc', 'M.Sc'), 
                                                                ('B.Com', 'B.Com'), 
                                                                ('M.Com', 'M.Com'), 
                                                                ('B.A', 'B.A'), 
                                                                ('M.A', 'M.A')))
    
    stream = models.CharField(max_length=100,choices=(('Civil', 'Civil'), ('Taxation', 'Taxation'),('AI', 'AI'), ('General', 'General'), ('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Computer Science', 'Computer Science'), ('Electronics', 'Electronics'), ('Chemical', 'Chemical'), ('Biotechnology', 'Biotechnology'))
                              )
    student_roll = models.CharField(max_length=100)
    student_dob = models.DateField()
    verified = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='teacher')
    teacher_id = models.CharField(max_length=100)
    teacher_dob = models.DateField()
    teacher_qualification = models.CharField(max_length=100)
    teacher_experience = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
