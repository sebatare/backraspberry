from django.urls import path

from .views import IndexView, ProjectDetailView, ProjectsListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
]
