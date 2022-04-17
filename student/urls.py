from django.urls import path

from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
)

app_name = "Student"

urlpatterns = [
    path("list/", StudentListView.as_view(), name="list"),
    path("detail/<int:id>/", StudentDetailView.as_view(), name="detail"),
    path("delete/<int:id>/", StudentDeleteView.as_view(), name="delete"),
    path("update/<int:id>", StudentUpdateView.as_view(), name="update"),
    path("create/", StudentCreateView.as_view(), name="create"),
]
