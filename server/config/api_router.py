from django.conf import settings
from django.conf.urls import url
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from transparencyportal.users.api.views import UserViewSet
from transparencyportal.undp_projects.api.views import ProjectViewSet, ProjectInfoViewSet, ProjectActivityViewSet, \
    ProjectDecViewSet, ProjectIndicatorViewSet, RegionProjectListViewSet, OrgProjectListViewSet, \
    ProjectsBudgetRegionViewSet, ProjectsBudgetSectorViewSet, ProjectsBudgetRegionByYearViewSet, ProjectsBudgetSectorByYearViewSet, ProjectsStatusByYearViewSet

from transparencyportal.undp_projects.api.views import Project1ViewSet, Project2ViewSet, ProjectTViewSet, \
    ProjectRViewSet, RegionBudgetViewSet
from transparencyportal.undp_donors.api.views import DonorFundSplitUpViewSet
from transparencyportal.master_tables.api.views import RegionViewSet, OrganisationViewSet, RegionNameViewSet, \
    SectorNameViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("project-list", ProjectViewSet)
router.register("region-list", RegionViewSet)
router.register("region-name", RegionNameViewSet)
router.register("organisation-list", OrganisationViewSet)
router.register("sector-name", SectorNameViewSet)
router.register("project-info", ProjectInfoViewSet)
router.register("project-act", ProjectActivityViewSet, basename="ProjectActivity")
router.register("project-dec", ProjectDecViewSet, basename="ProjectDec")
router.register("project-ind", ProjectIndicatorViewSet, basename="ProjectIndicator")
router.register("region-project-list", RegionProjectListViewSet, basename="RegionProjectList")
router.register("org-project-list", OrgProjectListViewSet, basename="OrgProjectList")
router.register("projects-budget-region", ProjectsBudgetRegionViewSet)
router.register("projects-budget-sector", ProjectsBudgetSectorViewSet)
router.register("projects-budget-region-year", ProjectsBudgetRegionByYearViewSet)
router.register("projects-budget-sector-year", ProjectsBudgetSectorByYearViewSet)
router.register("projects-status-year", ProjectsStatusByYearViewSet)
router.register("project-list-T", Project1ViewSet)
router.register("project-list-E", Project2ViewSet)
router.register("project_aggregate", ProjectTViewSet)
router.register("sector_aggregate", ProjectRViewSet)
router.register("project_detail", ProjectRViewSet)
router.register("budget_sources", RegionBudgetViewSet)
router.register("fin_split_up", DonorFundSplitUpViewSet)


app_name = "api"
urlpatterns = [
] + router.urls
