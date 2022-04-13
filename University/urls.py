from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("master/", include("master.urls", namespace="Master")),
    path("course/", include("course.urls", namespace="Course")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("account/", include("account.urls", namespace="account")),
    path("", include("config.urls", namespace="config")),
]
if settings.DEBUG:
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
