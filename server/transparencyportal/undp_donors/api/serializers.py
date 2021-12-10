from rest_framework import serializers
from undp_donors.models import DonorFundSplitUp


class DonorFundSplitUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorFundSplitUp
        fields = ["project","organisation","budget"]

        extra_kwargs = {
            "url": {"view_name": "api:donors-detail", "lookup_field": "project"}
        }
