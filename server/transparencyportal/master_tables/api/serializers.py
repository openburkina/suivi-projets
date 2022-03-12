from django.contrib.auth import get_user_model
from rest_framework import serializers
from master_tables.models import Region, Organisation, Sector


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["name", "region_code"]

        extra_kwargs = {
            "url": {"view_name": "api:region-detail", "lookup_field": "name"}
        }


class RegionDetailSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Region
        fields = ["region_code", "name", "longitude", "latitude"]


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ["org_name", "ref_id"]

        extra_kwargs = {
            "url": {"view_name": "api:organisation-detail", "lookup_field": "ref_id"}
        }


class SectorNameSerializer(serializers.ModelSerializer):
    sector = serializers.ReadOnlyField()

    class Meta:
        model = Sector
        fields = ["code", "sector"]

