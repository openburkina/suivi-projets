
from django.db.models import Count,Sum
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from undp_projects.models import Project
from .serializers import ProjectSerializer
from .serializers import Project1Serializer,ProjectTSerializer, ProjectRSerializer, RegionBudgetSerializer


class ProjectViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.order_by("organisation").filter(activity_status__exact=1)
    lookup_field = "title"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class Project1ViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = Project1Serializer
    queryset = Project.objects.order_by("organisation").filter(activity_status__exact=0)
    lookup_field = "title"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = Project1Serializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectTViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectTSerializer
    queryset = Project.objects.values('organisation').annotate(count=Count('organisation'))
    lookup_field = "organisation"



    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectTSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectRViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectRSerializer
    queryset = Project.objects.values('operating_unit','organisation').annotate(count=Count('project_id'))
    lookup_field = "operating_unit"

    #queryset = Project.objects.order_by("operating_unit")
    #lookup_field = "organisation"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectRSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class RegionBudgetViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = RegionBudgetSerializer
    queryset = Project.objects.values('operating_unit').annotate(sum=Sum('budgetT'))
    lookup_field = "operating_unit"

    #queryset = Project.objects.order_by("operating_unit")
    #lookup_field = "organisation"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = RegionBudgetSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)




