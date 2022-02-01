from django.contrib.auth import get_user_model
from rest_framework import serializers
from undp_projects.models import Project




class ProjectSerializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.name')
    sector = serializers.ReadOnlyField(source='sector.sector')
    org_name = serializers.ReadOnlyField(source='organisation.org_name')

    class Meta:
        model = Project
        fields = ["project_id", "title", "org_name", "operating_unit", "sector", "region", "activity_status",
                  "budgetT"]

        extra_kwargs = {
            "url": {"view_name": "api:project-detail", "lookup_field": "organisation"}
        }


#class ProjetSerializer(serializers.ModelSerializer):
 #   class Meta:
 #       model = Project
 #       fields = '__all__'


class Project1Serializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.name')
    sector = serializers.ReadOnlyField(source='sector.sector')
    org_name = serializers.ReadOnlyField(source='organisation.org_name')

    class Meta:
        model = Project
        fields = ["project_id", "title", "org_name", "operating_unit", "sector", "region", "activity_status",
                  "budgetT"]

        extra_kwargs = {
            "url": {"view_name": "api:project-detail", "lookup_field": "organisation"}
        }


class Project2Serializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.name')
    sector = serializers.ReadOnlyField(source='sector.sector')
    org_name = serializers.ReadOnlyField(source='organisation.org_name')

    class Meta:
        model = Project
        fields = ["project_id", "title", "org_name", "operating_unit", "sector", "region", "activity_status",
                  "budgetT"]

        extra_kwargs = {
            "url": {"view_name": "api:project-detail", "lookup_field": "organisation"}
        }


#class ProjectTSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Project
#        fields = ["title", "organisation","activity_status"]

#        extra_kwargs = {
#            "url": {"view_name": "api:project-detail", "lookup_field": "organisation"}
#       }
class ProjectTSerializer(serializers.Serializer):
    organisation = serializers.CharField(max_length=20)
    count = serializers.CharField(max_length=20)

class ProjectRSerializer(serializers.Serializer):
    organisation = serializers.CharField(max_length=20)
    operating_unit = serializers.CharField(max_length=20)
    count = serializers.CharField(max_length=20)

class RegionBudgetSerializer(serializers.Serializer):
    operating_unit = serializers.CharField(max_length=20)
    sum = serializers.CharField(max_length=20)






