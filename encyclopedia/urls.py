from os import name
from turtle import title
from django.urls import path

from encyclopedia import util

from . import views
urlpatterns = [
    path("wiki/<entry>/", views.singal_page, name="singal_page"),
    path("createPage/", views.createPage, name="createPage"),
    path("wiki/<entry>/edit/", views.edit, name="edit"),
    path("wiki/TITLE", views.index, name="index"),
    path("random/", views.randomPage, name="random"),
    path("search/", views.search , name = "search")
]

