from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    View,
)

from .forms import StudentForm
from .models import Student

user = get_user_model()


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = "student/list.html"


class StudentDetailView(DetailView):
    model = Student
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "student/detail.html"


class StudentDeleteView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect("")


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("")
    template_name = "student/create.html"

    def form_valid(self, form):
        new_form = form.save(commit=False)
        cd = form.cleaned_data
        user_obj = user.objects.create_user(
            national_code=cd["national_code"],
            first_name=cd["first_name"],
            last_name=cd["last_name"],
            phone_number=cd["phone_number"],
        )
        new_form.user = user_obj
        new_form.save()
        messages.success(self.request, "", "btn btn-success")
        return super(StudentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "", "btn btn-danger")
        return super(StudentCreateView, self).form_invalid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("")
    template_name = "student/update.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def form_invalid(self, form):
        new_form = form.save(commit=False)
        cd = form.cleaned_data
        user_obj = get_object_or_404(user, id=self.kwargs.get("id"))
        # user_obj.
        new_form.user = user_obj
        new_form.save()
        messages.success(self.request, "", "btn btn-success")
        return super(StudentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        messages.success()
        return super(StudentUpdateView, self).form_valid(form)
