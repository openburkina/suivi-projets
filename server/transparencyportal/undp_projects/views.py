from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.generic.list import ListView
from undp_projects.models import Project

from django.utils import timezone


class ProjetListView(ListView):

    model = Project
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProjectListView(LoginRequiredMixin, SuccessMessageMixin, DetailView):

    model = Project
    fields = ["name"]
    success_message = _("Information")






    def get_success_url(self):
        return self.request.project.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.project


project_list_view = ProjectListView.as_view()

