from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View, FormView

from extenstion.mixins import AdminUserMixin

from .forms import CourseCreateForm, CourseUpdateForm
from .models import Course
from student.models import Student


# Create your views here.


class CourseListView(AdminUserMixin, ListView):
    model = Course
    template_name = "course/list.html"


class CourseDetailView(AdminUserMixin, DetailView):
    model = Course
    template_name = "course/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


class CourseCreateView(CreateView):
    model = Course
    template_name = "course/create.html"
    success_url = reverse_lazy("course:course_list")
    form_class = CourseCreateForm


class CourseUpdateView(AdminUserMixin, UpdateView):
    model = Course
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "course/update.html"
    form_class = CourseUpdateForm

    def get_success_url(self):
        return reverse("course:course_detail", kwargs=[self.object.id])


class CourseDeleteView(AdminUserMixin, View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return redirect("Course:Course_list")


class CourseParticipationAdd(View):
    def get(self, request, course_id, student_id):
        student = get_object_or_404(Student, id=student_id)
        course = get_object_or_404(Course, id=course_id)
        course.participation.add(student)
        course.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
