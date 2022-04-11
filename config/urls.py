from django.urls import path
from .views import (
    PanelView,
)

app_name = "Config"

urlpatterns = [
    path('', PanelView.as_view(), name="Panel"),
]
