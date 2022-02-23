from django.contrib.auth import get_user_model
from rest_framework import serializers
from undp_projects.models import Project, ProjectActivity, ProjectDec, ProjectIndicator, Sector, Region


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


class ProjectInfoSerializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.name')
    sector = serializers.ReadOnlyField(source='sector.sector')
    org_name = serializers.ReadOnlyField(source='organisation.org_name')

    class Meta:
        model = Project
        fields = ["project_id", "title", "org_name", "budgetT", "region", "sector", "operating_unit", "activity_status",
                  "start_date", "finish_date"]

        extra_kwargs = {
            "url": {"view_name": "api:project-detail", "lookup_field": "organisation"}
        }


class ProjectActivitySerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = ProjectActivity
        fields = ["project_id", "title", "start_date", "finish_date", "amount_act", "Actors_execution",
                  "Actors_partner", "year_plan"]

        extra_kwargs = {
            "url": {"view_name": "api:project-act", "lookup_field": "project_id"}
        }


class ProjectDecSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = ProjectDec
        fields = ["project_id", "title", "dec_date", "amount_dec", "deliverable"]

        extra_kwargs = {
            "url": {"view_name": "api:project-act", "lookup_field": "project_id"}
        }


class ProjectIndicatorSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='project.title')

    class Meta:
        model = ProjectIndicator
        fields = ["project_id", "title", "reference", "reference_period", "target", "target_period", "target_status"]

        extra_kwargs = {
            "url": {"view_name": "api:project-ind", "lookup_field": "project_id"}
        }


class RegionProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["project_id", "beneficiary", "title", "sector", "organisation", "budgetT", "stage", "start_date",
                  "finish_date"]

        extra_kwargs = {
            "url": {"view_name": "api:region-project-list", "lookup_field": "region"}
        }


class OrgProjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["project_id", "beneficiary", "title", "sector", "region", "budgetT", "stage", "start_date",
                  "finish_date"]

        extra_kwargs = {
            "url": {"view_name": "api:org-project-list", "lookup_field": "organisation"}
        }


class ProjectsBudgetRegionSerializer(serializers.Serializer):
    region = serializers.StringRelatedField()
    sum = serializers.CharField(max_length=20)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectsBudgetRegionByYearSerializer(serializers.Serializer):
    region = serializers.StringRelatedField()
    sum = serializers.CharField(max_length=20)
    year = serializers.CharField(max_length=20)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectsBudgetSectorByYearSerializer(serializers.Serializer):
    sector = serializers.StringRelatedField()
    sum = serializers.CharField(max_length=20)
    year = serializers.CharField(max_length=20)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectsBudgetStatusByYearSerializer(serializers.Serializer):
    activity_status = serializers.CharField(max_length=20)
    sum = serializers.CharField(max_length=20)
    year = serializers.CharField(max_length=20)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectsBudgetSectorSerializer(serializers.Serializer):
    sector = serializers.StringRelatedField()
    sum = serializers.CharField(max_length=20)

    class Meta:
        model = Project
        fields = ['sector', 'sum']

# class ProjetSerializer(serializers.ModelSerializer):
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


# class ProjectTSerializer(serializers.ModelSerializer):
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
    region = serializers.ReadOnlyField(source='region.name')
    sector = serializers.ReadOnlyField(source='sector.sector')
    org_name = serializers.ReadOnlyField(source='organisation.org_name')

    class Meta:
        model = Project
        fields = ["project_id", "title", "org_name", "operating_unit", "sector", "region", "activity_status",
                  "budgetT"]
