from django.urls import path
from .views import (
    MasterListView,
    MasterCreateView,
    MasterUpdateView,
    MasterDeleteView,
    MasterDetailView,

)

app_name = "Master"

urlpatterns = [
    path('', MasterListView.as_view(), name='master_list'),
    path('<int:id>/', MasterDetailView.as_view(), name='master_detail'),
    path('update/<int:id>/', MasterUpdateView.as_view(), name='master_update'),
    path('delete/<int:id>/', MasterDeleteView.as_view(), name='master_delete'),
    path('create/', MasterCreateView.as_view(), name='master_create'),
]
