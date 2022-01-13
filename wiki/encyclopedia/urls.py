from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("results", views.results, name="results"),
    path("entry/create", views.create, name="create")
]
