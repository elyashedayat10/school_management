from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,

)
from django.http import Http404
from django.urls import reverse_lazy
from .forms import SiteSettingForm
from .models import SiteSetting, IPAddress
from django.contrib import messages
from extenstion.mixins import SuperuserMixin


# Create your views here.


class PanelView(TemplateView):
    template_name = "config/panel.html"


class SiteSettingCreateView(SuperuserMixin, CreateView):
    template_name = 'config/create.html'
    form_class = SiteSettingForm
    model = SiteSetting
    success_url = reverse_lazy()

    def dispatch(self, request, *args, **kwargs):
        ip_address = self.request.user.ip_address
        if IPAddress.objects.all().count() < 1:
            IPAddress.objects.create(ip_address=ip_address)
            return super(SiteSettingCreateView, self).dispatch(request, *args, **kwargs)
        raise Http404

    def form_valid(self, form):
        messages.success(self.request, '', '')
        return super(SiteSettingCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(SiteSettingCreateView, self).form_invalid(form)


class SiteSettingUpdateView(SuperuserMixin, UpdateView):
    template_name = 'config/update.html'
    form_class = SiteSettingForm
    model = SiteSetting
    success_url = reverse_lazy("config:Panel")
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, '', '')
        return super(SiteSettingUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(SiteSettingUpdateView, self).form_invalid(form)
