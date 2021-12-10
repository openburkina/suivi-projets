from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from transparencyportal.users.api.views import UserViewSet
from transparencyportal.undp_projects.api.views import ProjectViewSet
from transparencyportal.undp_projects.api.views import Project1ViewSet

from transparencyportal.undp_donors.api.views import DonorFundSplitUpViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("projets", ProjectViewSet)
router.register("projets1", Project1ViewSet)
router.register("fin_split_up", DonorFundSplitUpViewSet)


app_name = "api"
urlpatterns = router.urls
