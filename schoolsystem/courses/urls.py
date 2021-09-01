from django .urls import path
from .views import course_List, register_courses, register_courses
urlpatterns=[
    path("register/",register_courses,name="register_courses"),
    path("list/",course_List,name="course_List"),
    ]