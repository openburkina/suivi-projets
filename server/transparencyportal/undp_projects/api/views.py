from django.db.models import Count, Sum
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from undp_projects.models import Project, ProjectParticipatingOrganisations, ProjectIndicator
from .serializers import ProjectSerializer, ProjectInfoSerializer, Project1Serializer, Project2Serializer, \
    ProjectTSerializer, ProjectRSerializer, RegionBudgetSerializer
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


class DetailProject(DetailView):
    model = Project
    context_object_name = 'p'


def ProjectDetailView(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'projects/detail_project.html', {'project': project})


def ProjectRegionView(request, region_id):
    projects = Project.objects.filter(region_id=region_id)
    return render(request, 'projects/region_projects.html', {'projects': projects})


def ProjectDecView(request, project_id):
    project = DonorFundSplitUp.objects.get(pk=project_id)
    output = Output.objects.filter(project=project_id)
    return render(request, 'projects/dec_project.html', {'project': project, 'output': output})


def ProjectOutputView(request, project_id):
    output = Output.objects.filter(pk=project_id)
    return render(request, 'projects/dec_project.html', {'output': output})


def ProjectActView(request, project_id):
    project = Project.objects.get(pk=project_id)
    part = ProjectParticipatingOrganisations.objects.filter(project=project_id)
    return render(request, 'projects/act_project.html', {'project': project, 'part': part})


def ProjectIndView(request, project_id):
    project = Project.objects.get(pk=project_id)
    ind = ProjectIndicator.objects.get(project=project_id)
    return render(request, 'projects/ind_project.html', {'project': project, 'ind': ind})


class ProjectInfoViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ProjectInfoSerializer
    queryset = Project.objects.all()
    lookup_field = "project_id"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = ProjectInfoSerializer(request.project, context={"request": request})
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
