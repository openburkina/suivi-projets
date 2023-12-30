from datetime import datetime

from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Sum,Count
from django.db.models.expressions import F, Value

from iati_activities.models import Activity, \
    Transaction, Indicator, Budget, Results, PlannedDisbursement,ActivityParticipatingOrg

from iati_activities.serializers import ActivitySerializer,\
    TransactionSerializer, IndicatorSerializer, \
        ResultsSerializer, PlannedDisbursementSerializer,TransactionActivitySerializer, OrganisationActivityByStatusSerializer,\
            OrganisationActivityByRegionSerializer, OrganisationActivityBySectorSerializer, OrganisationActivityByRegionTransactionSerializer, TransactionEcartSerializer, \
                HomeActivityByStatusSerializer, LocationSerializer, RegionActivityByStatusSerializer, \
                OrganisationActivityByRegionTransactionAllSerializer,ActivityDetailsSerializer,ActivityParticipatingOrgSerializer

from iati_referentiel.serializers import OrganizationSerializer

from iati_referentiel.models import Organization,\
        Location

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ActivityViews(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.filter(hierarchy=1).distinct('title')
    serializer_class = ActivitySerializer

class ActivityViewsAll(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all().distinct('title')
    serializer_class = ActivitySerializer

class ActivityDetailsViews(APIView):
    def get(self, request):
        queryset = Activity.objects.annotate(
            identifiant=F('id'),
            titre=F('title'),
            bailleur=F('organizationid__narrative'),
            executant=F('activityparticipatingorg__organizationid__narrative'),
            montant=F('activite_budget__value'),
            region=F('locationid__name'),
            secteur=F('sectorid__narrative'),
            conditions=F('conditionid__condition'),
            statut=F('activity_status'),
            datedebut=F('planned_start'),
            datefin=F('planned_end') 
        ).distinct('id')
        
        data = ActivityDetailsSerializer(queryset,many=True).data
        return Response(data)

class OrganisationViews(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    
class OrganisationBailleurViews(viewsets.ReadOnlyModelViewSet):
    queryset = ActivityParticipatingOrg.objects.filter(role='Funding').distinct('organizationid')
    serializer_class = ActivityParticipatingOrgSerializer


class RegionViews(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class TransactionViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)


class IndicatorViews(APIView):
    def get(self, request, activity_id):
        queryset = Indicator.objects.filter(resultsid__activityid=activity_id)
        data = IndicatorSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class RegionActivityViews(APIView):
    def get(self, request, region_id):
        queryset = Activity.objects.filter(locationid=region_id).annotate(
            identifiant=F('id'),
            titre=F('title'),
            bailleur=F('organizationid__narrative'),
            executant=F('activityparticipatingorg__organizationid__narrative'),
            montant=F('activite_budget__value'),
            region=F('locationid__name'),
            secteur=F('sectorid__narrative'),
            conditions=F('conditionid__condition'),
            statut=F('activity_status'),
            datedebut=F('planned_start'),
            datefin=F('planned_end') 
        )
        
        data = ActivityDetailsSerializer(queryset,many=True).data
        return Response(data)

class TransactionRegionViews(APIView):
    def get(self, request, region_id):
        queryset = Transaction.objects.filter(activityid__locationid=region_id)
        queryset = queryset.annotate(name=F('organizationid2__narrative')).values('name')
        queryset =  queryset.annotate(value=Sum('value'), currency=F('currency'))                
        data = TransactionActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)
        
class ActivityResultatViews(APIView):
    def get(self, request, activity_id):
        queryset = Results.objects.filter(activityid=activity_id)
        data = ResultsSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)



#Activite d'une organisation
class OrganisationActivityViews(APIView):
    def get(self, request, organisation_id):
        queryset = Activity.objects.filter(organizationid=organisation_id).annotate(
            identifiant=F('id'),
            titre=F('title'),
            bailleur=F('organizationid__narrative'),
            executant=F('activityparticipatingorg__organizationid__narrative'),
            montant=F('activite_budget__value'),
            region=F('locationid__name'),
            secteur=F('sectorid__narrative'),
            conditions=F('conditionid__condition'),
            statut=F('activity_status'),
            datedebut=F('planned_start'),
            datefin=F('planned_end') 
        )
        
        data = ActivityDetailsSerializer(queryset,many=True).data
        return Response(data)

#Decaissement Activité
class ActivityDecaissementEcartViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id, transaction_type='Disbursement')
        queryset = queryset.annotate(valuedisbursement=Sum('value')).annotate(valueprevue=Sum('activityid__planneddisbursement__value')).annotate(difference=Sum('value')-Sum('activityid__planneddisbursement__value'))
        data = TransactionEcartSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)


#By Organisation And Status
class OrganisationActivityStatusViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)

        queryset = Budget.objects.filter(activityid__organizationid=organisation_id, activityid__planned_start__year=year)
        output = {
            'Identification': 0,
            'Implementation': 0,
            'Finalisation': 0,
            'Closed': 0,
            'Cancelled': 0,
            'Suspended': 0,
            'total': queryset.count(),
        }
        for query in queryset:
            output[query.activityid.activity_status] += 1
        data = OrganisationActivityByStatusSerializer(output).data
        return Response(data)

#By Organisation And Region
class OrganisationActivityRegionViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__organizationid=organisation_id, activityid__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__sectorid__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionSerializer(queryset, many=True).data
        return Response(data)

class ActivityChildViews(APIView):
    def get(self, request, activity_id):
        queryset = Activity.objects.filter(activityid=activity_id)
        data = ActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityDecaissementViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

#By Organisation And Sector
class OrganisationActivitySectorViews(APIView):
    def get(self, request, organisation_id):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        queryset = Budget.objects.filter(
            activityid__organizationid=organisation_id, 
            activityid__planned_start__year__gte=start_year, 
            activityid__planned_start__year__lte=end_year
            ).values('activityid__planned_start__year' , name=F('activityid__sectorid__narrative')).\
            annotate(value=Sum('value'))
        data = OrganisationActivityBySectorSerializer(queryset, many=True).data
        return Response(data)

#By Organisation And Region AND Transaction
class OrganisationActivityRegionTransactionViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__organizationid=organisation_id, activityid__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__locationid__name')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)


#By Home And Status
class HomeActivityStatusViews(APIView):
    def get(self, request):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__planned_start__year=year)
        output = {
            'Identification': 0,
            'Implementation': 0,
            'Finalisation': 0,
            'Closed': 0,
            'Cancelled': 0,
            'Suspended': 0,
            'total': queryset.count(),
        }
        for query in queryset:
            output[query.activityid.activity_status] += 1
        data = HomeActivityByStatusSerializer(output).data
        return Response(data)


#By Home Evolution And Sector
class HomeEvolutionSectorViews(APIView):
    def get(self, request):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        queryset = Budget.objects.filter(
            activityid__planned_start__year__gte=start_year, 
            activityid__planned_start__year__lte=end_year
            ).values('activityid__planned_start__year' , name=F('activityid__sectorid__narrative')).\
            annotate(value=Sum('value'))
        data = OrganisationActivityBySectorSerializer(queryset, many=True).data
        return Response(data)

#By Home And Region AND Transaction By Years
class HomeTransactionRegionTransactionViews(APIView):
    def get(self, request):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__locationid__name')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)

#By Home And Region AND Transaction All
class HomeTransactionRegionTransactionAllViews(APIView):
    def get(self, request):
        queryset = Budget.objects.all()
        queryset = queryset.annotate(identifiant=F('activityid__locationid__id'),name=F('activityid__locationid__name')).values('identifiant','name')
      #  queryset = queryset.annotate(boundary=F('activityid__locationid__boundary'))
        queryset = queryset.annotate(montant=Sum('value'),devise=F('currency'),)
        data = OrganisationActivityByRegionTransactionAllSerializer(queryset, many=True).data
        return Response(data)


#By Home And Sector AND Transaction
class HomeTransactionSectorTransactionViews(APIView):
    def get(self, request):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__sectorid__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)

#By Region And Status
class RegionActivityStatusViews(APIView):
    def get(self, request, region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__locationid=region_id, activityid__planned_start__year=year)
        output = {
            'Identification': 0,
            'Implementation': 0,
            'Finalisation': 0,
            'Closed': 0,
            'Cancelled': 0,
            'Suspended': 0,
            'total': queryset.count(),
        }
        for query in queryset:
            output[query.activityid.activity_status] += 1
        data = RegionActivityByStatusSerializer(output).data
        return Response(data)

#By Region And Sector
class RegionActivitySectorViews(APIView):
    def get(self, request, region_id):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        queryset = Budget.objects.filter(
            activityid__locationid=region_id, 
            activityid__planned_start__year__gte=start_year, 
            activityid__planned_start__year__lte=end_year
            ).values('activityid__planned_start__year' , name=F('activityid__sectorid__narrative')).\
            annotate(value=Sum('value'))
        data = OrganisationActivityBySectorSerializer(queryset, many=True).data
        return Response(data)

#By Region AND Transaction
class RegionActivityConditionTransactionViews(APIView):
    def get(self, request, region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__locationid=region_id, activityid__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__organizationid__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)

#By Region And Sector AND Transaction
class RegionTransactionSectorTransactionViews(APIView):
    def get(self, request,region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__planned_start__year=year, activityid__locationid=region_id)
        queryset = queryset.annotate(name=F('activityid__sectorid__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)
    
    


