from django.urls import path
from . import views
#list of accesbile urls, add these after /hello/
urlpatterns = [
    path("", views.index, name="index"),
    path("atul", views.atul, name="atul"),
    path("<str:name>", views.greet, name="greet") #now we can deal with any possible paths after /hello/
]

#empty url: visits views.index      index is name of the path
#include the urls file to Django urls.py


