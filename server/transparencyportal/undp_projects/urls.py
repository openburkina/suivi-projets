from django.urls import path
from undp_projects.views import ProjectListView, Project1ListView


app_name = "projects"
urlpatterns = [
    path("~list/", ProjectListView.as_view()),
    path("~list1/", Project1ListView.as_view()),
]


