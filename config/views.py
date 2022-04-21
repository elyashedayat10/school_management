from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,

)
from django.urls import reverse_lazy
from .forms import SiteSettingForm
from .models import SiteSetting
from django.contrib import messages
from extenstion.mixins import SuperuserMixin


# Create your views here.


class PanelView(TemplateView):
    template_name = "config/panel.html"


class SiteSettingCreateView(SuperuserMixin, CreateView):
    template_name = ''
    form_class = SiteSettingForm
    model = SiteSetting
    success_url = reverse_lazy()

    def form_valid(self, form):
        messages.success()
        return super(SiteSettingCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(SiteSettingCreateView, self).form_invalid(form)


class SiteSettingUpdateView(SuperuserMixin, UpdateView):
    template_name = ''
    form_class = SiteSettingForm
    model = SiteSetting
    success_url = reverse_lazy()
    slug_field = ''
    slug_url_kwarg = ''

    def form_valid(self, form):
        messages.success()
        return super(SiteSettingUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error()
        return super(SiteSettingUpdateView, self).form_invalid(form)


