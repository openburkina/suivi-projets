from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from master_tables.models import Region, Organisation, Sector
from .serializers import RegionSerializer, OrganisationSerializer, RegionDetailSerializer, SectorNameSerializer


class RegionViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    lookup_field = "name"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = RegionSerializer(request.region, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class RegionDetailViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = RegionDetailSerializer
    queryset = Region.objects.all()
    lookup_field = "region_code"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = RegionDetailSerializer(request.region, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class OrganisationViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
    lookup_field = "ref_id"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = OrganisationSerializer(request.organisation, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SectorNameViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = SectorNameSerializer
    queryset = Sector.objects.all()
    lookup_field = "code"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = SectorNameSerializer(request.region, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
