from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    View,
)
from django.views.generic.edit import FormMixin

from course.forms import InstituteCourseForm

from .forms import InstituteForm
from .models import Institute


class InstituteListView(ListView):
    model = Institute
    template_name = "Institute/list.html"


class InstituteDetailView(FormMixin, DetailView):
    model = Institute
    template_name = "Institute/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"
    form_class = InstituteCourseForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("institute:detail", args=[self.kwargs.get("id")])

    def form_valid(self, form):
        new_course = form.save(commit=False)
        new_course.institute = self.object
        new_course.save()
        print("ok" * 90)
        messages.success(self.request, "", "")
        return super(InstituteDetailView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "", "")
        return super(InstituteDetailView, self).form_invalid(form)


class InstituteCreateView(CreateView):
    model = Institute
    success_url = reverse_lazy("institute:list")
    form_class = InstituteForm
    template_name = "Institute/create.html"


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "Institute/update.html"
    success_url = reverse_lazy("institute:list")

    def get_success_url(self):
        return reverse("institute:detail", args=[self.kwargs.get("id")])


class InstituteDeleteView(View):
    def get(self, request, institute_id):
        institute = get_object_or_404(Institute, id=institute_id)
        institute.delete()
        return redirect("institute:list")
