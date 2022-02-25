from django.db.models.functions import ExtractYear
from django.views.generic import ListView
from django.db.models import Count, Sum
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from undp_projects.models import Project, ProjectActivity, ProjectDec, ProjectIndicator,\
    ProjectParticipatingOrganisations
from .serializers import ProjectSerializer, ProjectInfoSerializer, ProjectActivitySerializer, ProjectDecSerializer, \
    ProjectIndicatorSerializer, RegionProjectListSerializer, OrgProjectListSerializer, ProjectsBudgetRegionSerializer,\
    ProjectsBudgetSectorSerializer, ProjectsBudgetRegionByYearSerializer, \
    ProjectsBudgetSectorByYearSerializer, ProjectsStatusByYearSerializer,\
    Project1Serializer, Project2Serializer, ProjectTSerializer, ProjectRSerializer, RegionBudgetSerializer

from django.views.generic import DetailView
from undp_donors.models import DonorFundSplitUp
from undp_outputs.models import Output


class ProjectViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = "title"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectInfoViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectInfoSerializer
    queryset = Project.objects.all()
    lookup_field = "project_id"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectInfoSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectActivityViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectActivitySerializer
    lookup_field = "project_id"

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ProjectActivity.objects.all()
            pk = self.request.GET.get('q', None)
            if pk is not None:
                queryset = queryset.filter(project_id=pk)
            return queryset

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectActivitySerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectDecViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectDecSerializer
    lookup_field = "project_id"

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ProjectDec.objects.all()
            pk = self.request.GET.get('q', None)
            if pk is not None:
                queryset = queryset.filter(project_id=pk)
            return queryset

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectDecSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectIndicatorViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = ProjectIndicatorSerializer
    lookup_field = "project_id"

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = ProjectIndicator.objects.all()
            pk = self.request.GET.get('q', None)
            if pk is not None:
                queryset = queryset.filter(project_id=pk)
            return queryset

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectIndicatorSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RegionProjectListViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = RegionProjectListSerializer
    lookup_field = "region"

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Project.objects.all()
            pk = self.request.GET.get('q', None)
            if pk is not None:
                queryset = queryset.filter(region=pk)
            return queryset

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = RegionProjectListSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class OrgProjectListViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = OrgProjectListSerializer
    lookup_field = "organisation"

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Project.objects.all()
            pk = self.request.GET.get('q', None)
            if pk is not None:
                queryset = queryset.filter(organisation=pk)
            return queryset

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = OrgProjectListSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectsBudgetRegionViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectsBudgetRegionSerializer
    queryset = Project.objects.values('region').annotate(sum=Sum('budgetT'))

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectsBudgetRegionSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectsBudgetSectorViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectsBudgetSectorSerializer
    queryset = Project.objects.all().select_related('sector').annotate(sum=Sum('budgetT'))
    lookup_field = "sector"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectsBudgetSectorSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectsBudgetRegionByYearViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectsBudgetRegionByYearSerializer
    queryset = Project.objects.values('region').annotate(year=ExtractYear('start_date'), sum=Sum('budgetT'))
    lookup_field = "name"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectsBudgetRegionByYearSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectsBudgetSectorByYearViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectsBudgetSectorByYearSerializer
    queryset = Project.objects.values('sector').annotate(year=ExtractYear('start_date'), sum=Sum('budgetT'))
    lookup_field = "name"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectsBudgetSectorByYearSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProjectsStatusByYearViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectsStatusByYearSerializer
    queryset = Project.objects.values('activity_status').annotate(year=ExtractYear('start_date'), count=Count('project_id'))
    lookup_field = "name"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectsStatusByYearSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class Project1ViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = Project1Serializer
    queryset = Project.objects.order_by("organisation").filter(activity_status__exact=0)
    lookup_field = "title"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = Project1Serializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class Project2ViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = Project2Serializer
    queryset = Project.objects.order_by("organisation").filter(activity_status__exact=1)
    lookup_field = "title"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = Project2Serializer(request.project, context={"request": request})
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
    queryset = Project.objects.values('operating_unit', 'organisation').annotate(count=Count('project_id'))
    lookup_field = "operating_unit"

    # queryset = Project.objects.order_by("operating_unit")
    # lookup_field = "organisation"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectRSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RegionBudgetViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = RegionBudgetSerializer
    queryset = Project.objects.values('operating_unit').annotate(sum=Sum('budgetT'))
    lookup_field = "operating_unit"

    # queryset = Project.objects.order_by("operating_unit")
    # lookup_field = "organisation"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = RegionBudgetSerializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
