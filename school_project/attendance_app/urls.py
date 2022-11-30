from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.main_page),
    path("add_student", views.add_student),
    path("test", views.side_page)
]