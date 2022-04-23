from django.contrib import messages
from django.http import Http404
from django.db.models import Max, Min
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    View,
    UpdateView,
)

from extenstion.mixins import SuperuserMixin

from .forms import SiteSettingForm
from .models import IPAddress, SiteSetting
from student.models import (
    Student,
    Grade,
)
from master.models import Master
from institute.models import Institute
from django.contrib.auth import get_user_model
from course.models import Course

user = get_user_model()


# Create your views here.


class PanelView(View):
    def get(self, request):
        context = {
            'student_count': Student.objects.values('id').count(),
            'master_count': Master.objects.values('id').count(),
            'institute_count': Institute.objects.values('id').count(),
            'admin_count': user.objects.filter(is_admin=True).values('id').count(),
            'course_count': Course.objects.values('id').count(),
            'grade_count': Grade.objects.values('id').count(),
            'most_participation_course': Course.objects.annotate(
                Max('participation')),
            'less_participation_course': Course.objects.annotate(
                Min('participation')),
        }
        return render(request, 'config/panel.html', context)


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
