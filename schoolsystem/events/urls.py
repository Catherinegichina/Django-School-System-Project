from django .urls import path
from .views import event_List, register_events



urlpatterns=[
    path("register/",register_events,name="register_events"),
    path("list/",event_List,name="event_List"),]