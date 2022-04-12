from django.http import Http404


class AdminUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super(AdminUserMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404


class SuperuserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super(SuperuserMixin, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404
