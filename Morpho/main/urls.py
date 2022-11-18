from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), 
    path("home/", views.home, name="Home"),
    path("create/", views.create, name="Create"),
    path("write/<type>/", views.write, name="Write")
]