from django.shortcuts import render
from .forms import StudentRegistrationForm
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

