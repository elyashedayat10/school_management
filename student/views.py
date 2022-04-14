from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .forms import StudentForm
from .models import Student


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = ''


class StudentDetailView(DetailView):
    model = Student
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = ''


class StudentDeleteView(View):

    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('')


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('')
    template_name = ''

    def form_valid(self, form):
        messages.success()
        return super(StudentCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(StudentCreateView, self).form_invalid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('')
    template_name = ''
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def form_invalid(self, form):
        messages.error()
        return super(StudentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        messages.success()
        return super(StudentUpdateView, self).form_valid(form)
