from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.


class PanelView(TemplateView):
    template_name = 'config/panel.html'
