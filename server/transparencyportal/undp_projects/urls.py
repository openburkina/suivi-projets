from django.urls import path
from undp_projects.views import ProjectListView

app_name = "projects"
urlpatterns = [
    path("~list/", ProjectListView.as_view()),
]
