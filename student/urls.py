from django.urls import path

from .views import (
    GradeCreateView,
    GradeDeleteView,
    GradeListView,
    GradeUpdateView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentSelectView,
    StudentUpdateView,
)

app_name = 'Student'

urlpatterns = [
    path('list/', StudentListView.as_view(), name='list'),
    path('detail/<int:id>/', StudentDetailView.as_view(), name='detail'),
    path('delete/<int:id>/', StudentDeleteView.as_view(), name='delete'),
    path('update/<int:id>', StudentUpdateView.as_view(), name='update'),
    path('create/', StudentCreateView.as_view(), name='create'),
    path('grade_list/', GradeListView.as_view(), name='grade_list'),
    path('grade_create/', GradeCreateView.as_view(), name='grade_create'),
    path('grade_delete/<int:id>/', GradeDeleteView.as_view(), name='grade_delete'),
    path('grade_update/<int:id>/', GradeUpdateView.as_view(), name='grade_update'),
    path('select/', StudentSelectView.as_view(), name='select'),
]
