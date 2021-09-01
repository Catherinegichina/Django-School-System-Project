from django .urls import path
from .views import register_student, student_List
urlpatterns=[
    path("register/",register_student,name="register_student"),
    path("list/",student_List,name="student_list"),
# creating paths that got to our vuiews-line1
]
# step2:creata a new template