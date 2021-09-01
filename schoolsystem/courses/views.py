# from schoolsystem.courses.models import Courses
from django.shortcuts import render
from django.forms.forms import Form
from .forms import CoursesRegistrationForm
from .models import Courses

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form=CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:        
        form=CoursesRegistrationForm()
        
    return render(request,"register_courses.html",{"form":form})


def course_List(request):
    courses=Courses.objects.all()
    return render(request,"course_list.html",
    {"courses":courses})
