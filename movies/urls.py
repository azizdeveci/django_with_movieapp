from django.urls import path
from . import views

urlpatterns=[

    #http://127.0.0.1:8000/
    #http://127.0.0.1:8000/home
    #http://127.0.0.1:8000/movies


    path("",views.home),
    path("home",views.home),
    path("movies",views.movies)



]