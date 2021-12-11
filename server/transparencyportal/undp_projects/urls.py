from django.urls import path
from undp_projects.views import ProjectListView, Project1ListView
from undp_projects.api.views import TestListeView



app_name = "projects"
urlpatterns = [
    path("list/", ProjectListView.as_view()),
    path("list1/", Project1ListView.as_view()),
    path("projets_id/<nombre>", TestListeView.as_view()),

]


