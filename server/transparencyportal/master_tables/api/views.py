from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from master_tables.models import Region, Organisation
from .serializers import RegionSerializer, OrganisationSerializer


class RegionViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    lookup_field = "name"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = RegionSerializer(request.region, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class OrganisationViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
    lookup_field = "org_name"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = OrganisationSerializer(request.organisation, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)