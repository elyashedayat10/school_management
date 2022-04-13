from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from extenstion.mixins import AdminUserMixin

from .forms import CourseForm
from .models import Course

# Create your views here.


class CourseListView(AdminUserMixin, ListView):
    model = Course
    template_name = "course/course_list.html"


class CourseDetailView(AdminUserMixin, DetailView):
    model = Course
    template_name = "course/course_detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


class CourseCreateView(AdminUserMixin, CreateView):
    model = Course
    template_name = "course/course_create.html"
    success_url = reverse_lazy("course:course_list")
    form_class = CourseForm


class CourseUpdateView(AdminUserMixin, UpdateView):
    model = Course
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "course/course_update.html"
    form_class = CourseForm

    def get_success_url(self):
        return reverse("course:course_detail", kwargs=[self.object.id])


class CourseDeleteView(AdminUserMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return redirect("Course:Course_list")
