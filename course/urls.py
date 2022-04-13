from django.urls import path

from .views import (
    CourseCreateView,
    CourseDeleteView,
    CourseDetailView,
    CourseListView,
    CourseUpdateView,
)

app_name = "Course"

urlpatterns = [
    path("list/", CourseListView.as_view(), name="List"),
    path("create/", CourseCreateView.as_view(), name="Create"),
    path("update/<int:id>/", CourseUpdateView.as_view(), name="Update"),
    path("delete/<int:id>/", CourseDeleteView.as_view(), name="Delete"),
    path("detail/<int:id>/", CourseDetailView.as_view(), name="Detail"),
]
