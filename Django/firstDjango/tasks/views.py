from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #takes in a char field, with given prompt
    #priority = forms.IntegerField(label = "Priority", min_value=1, max_value=10)


# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method=='POST':
        form = NewTaskForm(request.POST) #POST has data submitted by user
        if form.is_valid(): #server side validation: e.g.priority range
            task = form.cleaned_data['task']
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
            "form": form,   #display their own form again
             })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm(),  #pass the form to html page
    })