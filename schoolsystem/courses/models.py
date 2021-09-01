from django.db import models
# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=12,null=True,blank=True)
    trainer=models.CharField(max_length=20,null=True,blank=True)
    syllabus=models.FileField(upload_to='documents/%y/%m/%d',null=True)
    course_code=models.CharField(max_length=12,null=True,blank=True)
    coursedescription=models.TextField(null=True,blank=True)


