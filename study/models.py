from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class StudyMaterials(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='study_materials')
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=255, choices=(('B.Tech', 'B.Tech'), 
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
                                                                ('M.A', 'M.A'),("Others","Others")))
    
    stream = models.CharField(max_length=100,choices=(('Civil', 'Civil'), ('Taxation', 'Taxation'),('AI', 'AI'), ('General', 'General'), ('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Computer Science', 'Computer Science'), ('Electronics', 'Electronics'), ('Chemical', 'Chemical'), ('Biotechnology', 'Biotechnology'),("Others","Others"))
                )
    category = models.CharField(choices=(("Assignment","Assignment"),("Notes","Notes"),("Others","Others"),("Project Contents","Project Contents")),max_length=100)
    description = RichTextField(null=True, blank=True)
    file = models.FileField(upload_to='study_materials')
    date = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


class Courses(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_query_name="owner")
    course_title = models.CharField(max_length=255)
    added_date = models.DateField(auto_now_add=True)
    description = models.TextField()

class Classes_for_Course(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course")
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to="course_video")
    material = models.FileField(upload_to="course_material")
    date = models.DateField(auto_now_add=True)

