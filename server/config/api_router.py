from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from transparencyportal.users.api.views import UserViewSet
from transparencyportal.undp_projects.api.views import ProjectViewSet
from transparencyportal.undp_projects.api.views import Project1ViewSet, Project2ViewSet, ProjectTViewSet, \
    ProjectRViewSet, RegionBudgetViewSet
from transparencyportal.undp_donors.api.views import DonorFundSplitUpViewSet
from transparencyportal.master_tables.api.views import RegionViewSet, OrganisationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

router.register("project-list", ProjectViewSet)
router.register("project-list-T", Project1ViewSet)
router.register("project-list-E", Project2ViewSet)
router.register("project_aggregate", ProjectTViewSet)
router.register("sector_aggregate", ProjectRViewSet)
router.register("budget_sources", RegionBudgetViewSet)

router.register("fin_split_up", DonorFundSplitUpViewSet)

router.register("region-list", RegionViewSet)
router.register("organisation-list", OrganisationViewSet)

app_name = "api"
urlpatterns = router.urls
