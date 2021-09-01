# from schoolsystem.events.models import Events
from django.shortcuts import render
from django.forms.forms import Form
from .forms import EventsRegistrationForm
from .models import Events

# Create your views here.
def register_events(request):
    form=EventsRegistrationForm()
    return render(request,"register_events.html",{"form":form})

def register_events(request):
    if request.method =="POST":
        # after the user posts their request.
        form=EventsRegistrationForm(request.POST ,request.FILES)
        # and the infor is true,we save the file.
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
           
        form=EventsRegistrationForm()
    return render(request,"register_events.html",{"form":form})

def event_List(request):
    events=Events.objects.all()
    return render(request,"events_list.html",
    {"events":events})
