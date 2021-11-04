from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from undp_projects.models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.order_by("organisation").filter(activity_status__exact=1)
    lookup_field = "title"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
