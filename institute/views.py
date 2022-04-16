from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
# Create your views here.
from .models import Institute
from .forms import InstituteForm


class InstituteListView(ListView):
    model = Institute
    template_name = 'Institute/'


class InstituteDetailView(DetailView):
    model = Institute
    template_name = 'Institute/'
    slug_field = 'id'
    slug_url_kwarg = 'id'


class InstituteCreateView(CreateView):
    model = Institute
    success_url = reverse_lazy('')
    form_class = InstituteForm
    template_name = 'Institute/'


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'Institute/'

    def get_success_url(self):
        pass


class InstituteDeleteView(View):
    def get(self, request, institute_id):
        institute = get_object_or_404(Institute, id=institute_id)
        institute.delete()
        return redirect('')
