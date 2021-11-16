from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from transparencyportal.users.api.views import UserViewSet
from transparencyportal.undp_projects.api.views import ProjectViewSet
from transparencyportal.undp_projects.api.views import Project1ViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("projets", ProjectViewSet)
router.register("projets1", Project1ViewSet)



app_name = "api"
urlpatterns = router.urls
