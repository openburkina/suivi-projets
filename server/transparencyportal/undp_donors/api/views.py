from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from undp_donors.models import DonorFundSplitUp

from .serializers import DonorFundSplitUpSerializer


class DonorFundSplitUpViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = DonorFundSplitUpSerializer
    queryset = DonorFundSplitUp.objects.order_by("project")
    lookup_field = "project"


    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = DonorFundSplitUpSerializer(request.DonorFundSplitUp, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


