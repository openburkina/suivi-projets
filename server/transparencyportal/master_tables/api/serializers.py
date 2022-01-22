from django.contrib.auth import get_user_model
from rest_framework import serializers
from master_tables.models import Region, Organisation


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["name", "region_code"]

        extra_kwargs = {
            "url": {"view_name": "api:region-detail", "lookup_field": "name"}
        }


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ["org_name", "ref_id"]

        extra_kwargs = {
            "url": {"view_name": "api:organisation-detail", "lookup_field": "org_name"}
        }
