from django.urls import path

from . import views

urlpatterns = [
    path("wiki/<str:name>", views.converter, name="converter"),
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("newpage/", views.new_page, name="newpage"),
    path("edit/", views.edit_page, name="edit"),
    path("save/", views.save_page,name="savepage"),
    path("random/",views.random_page, name="randompage")
]
