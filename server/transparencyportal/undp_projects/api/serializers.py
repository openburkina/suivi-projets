from django.contrib.auth import get_user_model
from rest_framework import serializers
from undp_projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "description", "organisation","activity_status"]

        extra_kwargs = {
            "url": {"view_name": "api:project-detail", "lookup_field": "organisation"}
        }


class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class Project1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "description", "organisation","activity_status"]

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






