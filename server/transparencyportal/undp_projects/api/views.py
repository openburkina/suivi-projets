from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from undp_projects.models import Project
from .serializers import ProjectSerializer, ProjetSerializer
from .serializers import Project1Serializer
from rest_framework.views import APIView

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetSerializer
    queryset = Project.objects.all()
     

class TestListeView(APIView):
    def post(self, request,serializer_class = ProjetSerializer, nombre=None):
        
        if nombre:
            queryset = Project.objects.filter(pk = nombre)
        else:
            queryset = Project.objects.all()
        serializer = serializer_class(queryset)
        return Response({
           'entities':serializer.data, 
            })
   

class Project1ViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = Project1Serializer
    queryset = Project.objects.order_by("organisation").filter(activity_status__exact=0)
    lookup_field = "title"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = Project1Serializer(request.project, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
