from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from .models import Master
from .forms import MasterForm


# Create your views here.

class MasterListView(ListView):
    model = Master
    template_name = 'master/master_list.html'


class MasterDetailView(DetailView):
    model = Master
    template_name = 'master/master_detail.html'
    slug_field = ''
    slug_url_kwarg = ''


class MasterCreateView(CreateView):
    model = Master
    template_name = 'master/master_create.html'
    success_url = reverse_lazy('')
    form_class = MasterForm


class MasterUpdateView(UpdateView):
    model = Master
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'master/master_update.html'
    success_url = reverse_lazy('')
    form_class = MasterForm


class MasterDeleteView(View):
    def get(self, request, master_id):
        master = get_object_or_404(Master, id=master_id)
        master.delete()
        return redirect('')
