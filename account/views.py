from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    View,
)
from django.urls import reverse, reverse_lazy
from extenstion.mixins import SuperuserMixin

user = get_user_model()
from .forms import LoginForm, AdminCreateForm, AdminUpdateForm


# Create your views here.


class UserLoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(UserLoginView, self).dispatch(*request, *args, **kwargs)
        else:
            return redirect()

    form_class = LoginForm
    template_name = 'account/'

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, national_code=cd['national_code'], password=cd['password'])
            if user:
                login(request, user)
                messages.success(request, 'با موفقیت وارد حساب خود شدید', 'btn btn-success')
                if user.is_admin:
                    return redirect('')
                return redirect('')
            else:
                messages.error(request, 'هیچ کاربری یا این اطلاعات وجود ندارد')
                return redirect('')


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت از حساب خود خارح شدید')
        return redirect()


# admin views
class AdminListView(ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = 'account/'


class AdminDeleteView(SuperuserMixin, View):

    def get(self, request, admin_id):
        admin_user = get_object_or_404(user, id=admin_id)
        admin_user.delete()
        messages.success(request, 'ادمین مورد نظر با موفقیت حذف شد', 'btn btn-success')
        return redirect('')


class AdminCreateView(SuperuserMixin, CreateView):
    model = user
    form_class = AdminCreateForm
    template_name = 'account/'
    success_url = reverse_lazy()

    def form_valid(self, form):
        messages.success(self.request, '', '')
        return super(AdminCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(AdminCreateView, self).form_invalid(form)


class AdminUpdateView(SuperuserMixin, UpdateView):
    model = user
    form_class = AdminUpdateForm
    template_name = 'account/'
    success_url = reverse_lazy()

    def form_valid(self, form):
        messages.success(self.request, '', '')
        return super(AdminUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '', '')
        return super(AdminUpdateView, self).form_invalid(form)


class AdminDetailView(SuperuserMixin, DetailView):
    model = user
    slug_field = ''
    slug_url_kwarg = ''
    template_name = 'account/'
