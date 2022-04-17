from django.urls import path

from .views import (
    InstituteCreateView,
    InstituteDeleteView,
    InstituteDetailView,
    InstituteListView,
    InstituteUpdateView,
)

app_name = "institute"

urlpatterns = [
    path("list", InstituteListView.as_view(), name="list"),
    path("detail/<int:id>/", InstituteDetailView.as_view(), name="detail"),
    path("delete/<int:institute_id>/", InstituteDeleteView.as_view(), name="delete"),
    path("update/<int:id>/", InstituteUpdateView.as_view(), name="update"),
    path("create/", InstituteCreateView.as_view(), name="create"),
]
