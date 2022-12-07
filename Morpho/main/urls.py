from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="index"), 
    path("home/", views.home, name="Home"),
    path("create/", views.create, name="Create"),
    path("create/<str:type>/", views.create_type, name="CreateType"),
    path("view/", views.view, name="View"),
    path("view/<str:type>/<int:id>",views.viewCreation, name="ViewCreation"),
    path("compile/choose_container/", views.chooseContainer, name="ChooseContainer"),
    path("compile/choose_container/<str:type>/<int:id>/choose_components/",views.chooseComponents, name="ChooseComponents"),
    path("compile/finishCompile", views.Compile, name="Compile"),
]