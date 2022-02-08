from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from transparencyportal.users.api.views import UserViewSet
from transparencyportal.undp_projects.api.views import ProjectViewSet, ProjectInfoViewSet
from transparencyportal.undp_projects.api.views import Project1ViewSet, Project2ViewSet, ProjectTViewSet, \
    ProjectRViewSet, RegionBudgetViewSet, ProjectDetailView, ProjectRegionView, ProjectDecView, ProjectActView, ProjectIndView, ProjectOutputView
from transparencyportal.undp_donors.api.views import DonorFundSplitUpViewSet
from transparencyportal.master_tables.api.views import RegionViewSet, OrganisationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("project-list", ProjectViewSet)
router.register("project-info", ProjectInfoViewSet)
router.register("project-list-T", Project1ViewSet)
router.register("project-list-E", Project2ViewSet)
router.register("project_aggregate", ProjectTViewSet)
router.register("sector_aggregate", ProjectRViewSet)
router.register("project_detail", ProjectRViewSet)
router.register("budget_sources", RegionBudgetViewSet)
router.register("fin_split_up", DonorFundSplitUpViewSet)
router.register("region-list", RegionViewSet)
router.register("organisation-list", OrganisationViewSet)

app_name = "api"
urlpatterns = [
    path('project-detail/<int:project_id>', ProjectDetailView, name='project-detail'),
    path('project-region/<int:region_id>', ProjectRegionView, name='project-region'),
    path('project-output/<int:project_id>', ProjectOutputView, name='project-output'),
    path('project-dec/<int:project_id>', ProjectDecView, name='project-dec'),
    path('project-act/<int:project_id>', ProjectActView, name='project-act'),
    path('project-ind/<int:project_id>', ProjectIndView, name='project-ind'),
] + router.urls
