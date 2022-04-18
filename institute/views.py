from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import InstituteForm

# Create your views here.
from .models import Institute


class InstituteListView(ListView):
    model = Institute
    template_name = "Institute/list.html"


class InstituteDetailView(DetailView):
    model = Institute
    template_name = "Institute/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"


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
        return reverse('institute:detail', args=[self.kwargs.get('id')])


class InstituteDeleteView(View):
    def get(self, request, institute_id):
        institute = get_object_or_404(Institute, id=institute_id)
        institute.delete()
        return redirect("institute:list")
