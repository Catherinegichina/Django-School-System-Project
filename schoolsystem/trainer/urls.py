from django .urls import path
from .views import register_trainer, trainer_List
urlpatterns=[
    path("register/",register_trainer,name="register_trainer"),
    path("list",trainer_List,name="trainer_List"),
]