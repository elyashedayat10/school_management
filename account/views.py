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
from .forms import LoginForm, AdminCreateForm, AdminUpdateForm

user = get_user_model()


# Create your views here.


class UserLoginView(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super(UserLoginView, self).dispatch(*request, *args, **kwargs)
        else:
            return redirect('config:Panel')

    form_class = LoginForm
    template_name = 'account/login.html'

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
                return redirect('config:Panel')
            else:
                messages.error(request, 'هیچ کاربری یا این اطلاعات وجود ندارد')
                return redirect('')


class UserLogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت از حساب خود خارح شدید')
        return redirect('account:login')


# admin views
class AdminListView(ListView):
    queryset = user.objects.filter(is_admin=True)
    template_name = 'account/admin_list.html'


class AdminCreateView(SuperuserMixin, CreateView):
    model = user
    form_class = AdminCreateForm
    template_name = 'account/admin_create.html'
    success_url = reverse_lazy('account:admin_list')

    def form_valid(self, form):
        messages.success(self.request, 'ادمین با موفقیت اضافه شد', 'btn btn-success')
        return super(AdminCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'خطا در وزود اطلاعات', 'btn btn-danger')
        return super(AdminCreateView, self).form_invalid(form)


class AdminUpdateView(SuperuserMixin, UpdateView):
    model = user
    form_class = AdminUpdateForm
    template_name = 'account/admin_update.html'
    success_url = reverse_lazy('account:admin_list')

    def form_valid(self, form):
        messages.success(self.request, 'به روزرسانی با موفیت انحام شد', 'btn btn-success')
        return super(AdminUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'خطلا در بروزرسانی', 'btn btn-danger')
        return super(AdminUpdateView, self).form_invalid(form)


class AdminDetailView(SuperuserMixin, DetailView):
    model = user
    slug_field = 'id'
    slug_url_kwarg = 'id'
    template_name = 'account/admin_detail.html'


class UserDeleteView(SuperuserMixin, View):

    def get(self, request, admin_id):
        admin_user = get_object_or_404(user, id=admin_id)
        admin_user.delete()
        messages.success(request, 'ادمین مورد نظر با موفقیت حذف شد', 'btn btn-success')
        return redirect('account:admin_list')
