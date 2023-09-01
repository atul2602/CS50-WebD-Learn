from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    # which link should prompt this response? add it to urls.py
    return render(request, "hello/index.html")

# we can create multiple views
def atul(request):
    return HttpResponse("Hello Atul!")

#paramterised view
# def greet(request, name):
#     return HttpResponse(f"Hello ,{name}")

# support for variables on top of HTML
def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize(),
        
    })