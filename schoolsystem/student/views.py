
from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Student
# 2.Views
# import forms from the current directory.
# view,accept,response.
# create a function for the http rqst.
# form-instance of our form.
# a http rqst,where do you want the rqst to be sent,result message/response.
# 3.Next is a url.
def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"register_students.html",{"form":form})

def register_student(request):
    if request.method =="POST":
        # after the user posts their request.
        form=StudentRegistrationForm(request.POST,request.FILES)
        # and the infor is true,we save the file.
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
           
        form=StudentRegistrationForm()
    return render(request,"register_students.html",{"form":form})

def student_List(request):
    students=Student.objects.all()
    return render(request,"student_list.html",
    {"students":students})
# Part 1 plus import.Add paths at urls.py
