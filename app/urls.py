from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name="home"),
    path("save/",savedata,name="savedata"),
    path("delete/<int:rahul>/",deletedata,name="delete"),
    path("edit/<int:rahul>/",editdata,name="edit"),
    # path("updatedata/",updatedata,name="editdata"),

]