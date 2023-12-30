from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from rest_framework.response import Response
from iati_referentiel.models import CollaborationType, Country , DefaultAidType, \
    DefaultFinanceType, HumanitarianScope, Location, Organization, Region, Sector, Tag, Condition

from .constants import STATUS,ROLE,TYPE,TRANSACTION,MEASURE,DATETYPE,BUDGESTATUT,BUDGETYPE,BUDGETNOTAPPRO

class ActivityParticipatingOrg(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True,choices=ROLE,verbose_name ='Rôle')
    organizationid = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organizationid', verbose_name ='Organisation')
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid',verbose_name ='Projet')

    class Meta:
        verbose_name = 'Organisme Participant'
        verbose_name_plural = 'Organismes Participants'

    def __str__(self):
        return '%s - %s (%s)' % (self.activityid, self.role, self.organizationid)

class ActualDocumentLink(models.Model):
    actualid = models.OneToOneField('Actual', models.DO_NOTHING, db_column='actualid', primary_key=True)
    document_linkid = models.ForeignKey('DocumentLink', models.DO_NOTHING, db_column='Document-linkID',verbose_name='Lien Document')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        unique_together = (('actualid', 'document_linkid'),)
        verbose_name = 'Document Réel'
        verbose_name_plural = 'Documents Réel'


class BaselineDocumentLink(models.Model):
    baselineid = models.OneToOneField('Baseline', models.DO_NOTHING, db_column='baselineid', primary_key=True)
    document_linkid = models.ForeignKey('DocumentLink', models.DO_NOTHING, db_column='Document-linkID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        unique_together = (('baselineid', 'document_linkid'),)


class ContactInfo(models.Model):
    organizationid = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organizationid')
    person_name = models.CharField(db_column='Person-name', max_length=255, blank=True, null=True,verbose_name='Nom et Prenom(s)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    job_title = models.CharField(db_column='Job-title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True,verbose_name='Site Web')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    def __str__(self):
        return '%s - %s - %s' % (self.person_name, self.job_title, self.organizationid.ref)


class DefaultFinanceTypeActivity(models.Model):
    default_finance_typeid = models.OneToOneField(DefaultFinanceType, models.DO_NOTHING, db_column='Default-finance-typeID', primary_key=True,verbose_name ='Type Financement')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')

    class Meta:
        unique_together = (('default_finance_typeid', 'activityid'),)
        verbose_name = 'Type de finance par défaut'
        verbose_name_plural = 'Type de finance par défaut'


class DocumentLink(models.Model):
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')
    url = models.CharField(max_length=500, blank=True, null=True)
    format = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Lien Document'
        verbose_name_plural = 'Lien Document'


class DocumentLinkIndicator(models.Model):
    document_linkid = models.OneToOneField(DocumentLink, models.DO_NOTHING, db_column='Document-linkID', primary_key=True,verbose_name ='Lien document')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indicatorid = models.ForeignKey('Indicator', models.DO_NOTHING, db_column='indicatorid',verbose_name ='Indicateur')

    class Meta:
        unique_together = (('document_linkid', 'indicatorid'),)
        verbose_name = 'Document Indicateur'
        verbose_name_plural = 'Document Indicateur'


class DocumentLinkResults(models.Model):
    document_linkid = models.OneToOneField(DocumentLink, models.DO_NOTHING, db_column='Document-linkID', primary_key=True,verbose_name ='Lien Document')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resultsid = models.ForeignKey('Results', models.DO_NOTHING, db_column='resultsid',verbose_name ='Resultat')

    class Meta:
        unique_together = (('document_linkid', 'resultsid'),)
        verbose_name = 'Document Résultat'
        verbose_name_plural = 'Document Résultat'

class PlannedDisbursement(models.Model):
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid',verbose_name ='Activité')
    type = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Type')
    period_start = models.DateField(db_column='Period-start', blank=True, null=True,verbose_name ='Période Debut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end = models.DateField(db_column='Period-end', blank=True, null=True,verbose_name ='Période Fin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.FloatField(verbose_name ='Montant')
    currency = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Dévide')
    value_date = models.DateField(db_column='Value-date',blank=True, null=True,verbose_name ='Valeur Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        verbose_name = 'Décaissement Prévu'
        verbose_name_plural = 'Décaissement Prévus'


class Transaction(models.Model):
    regionid3 = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid3',verbose_name ='Région')
    countryid3 = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryid3',verbose_name ='Pays')
    organizationid2 = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organizationid2',related_name='provider',verbose_name ='Donneur')
    organizationid = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organizationid',related_name='receiver',verbose_name ='Receveur')
    activityid = models.OneToOneField('Activity', related_name='activite_transaction', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='activityid')
    iati_identifier = models.BigIntegerField(db_column='Iati-identifier',editable=False, unique=True)
    ref = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Réference')
    humanitarian = models.BooleanField(verbose_name ='Humanitaire')
    transaction_type = models.CharField(db_column='Transaction-type', max_length=255, blank=True, null=True,choices=TRANSACTION,verbose_name ='Type Transaction')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_date = models.DateField(db_column='Transaction-date',verbose_name ='Date Transaction')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.FloatField(verbose_name ='Montant')
    currency = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Dévise')
    sectorid = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sectorid',related_name='secteur',verbose_name='Secteur')
    value_date = models.DateField(db_column='Value-date',verbose_name ='Date Montant')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Description')
    disbursement_channel = models.CharField(db_column='Disbursement-channel', max_length=255, blank=True, null=True,verbose_name ='Chaîne de distribution')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
    def __str__(self):
        return '%s - %s -%s' % (self.ref, self.value,self.currency)



class Activity(models.Model):
    regionid3 = models.ForeignKey(Region, models.DO_NOTHING, db_column='regionid3',verbose_name ='Région')
    countryid3 = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryid3',verbose_name ='Pays')
    locationid = models.ManyToManyField(Location, blank=True, null=True, verbose_name='Localisation',related_name='as_location_activity')
    sectorid = models.ManyToManyField(Sector, verbose_name ='Secteur',related_name='as_sector_activity')
    activityid = models.ForeignKey('self', models.DO_NOTHING, db_column='activityid', blank=True, null=True,verbose_name ='Projet Parent')
    organizationid = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organizationid',related_name='bailleuractivite',verbose_name='Bailleur')
    contact_infoid = models.ForeignKey(ContactInfo, models.DO_NOTHING, db_column='Contact-infoID',blank=True, null=True,verbose_name ='Contact')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iati_identifier = models.CharField(db_column='Iati-identifier',max_length=255, blank=True, null=True,verbose_name ='Identifiant Iati')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, verbose_name ='Intitulé')
    conditionid = models.ManyToManyField(Condition, verbose_name='Condition',related_name='as_condition_activity')
    lang = models.CharField(max_length=255, blank=True, null=True,verbose_name='Language')
    default_currency = models.CharField(db_column='Default-currency', max_length=255, blank=True, null=True,verbose_name ='Dévise')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humanitarian = models.BooleanField(verbose_name ='Humanitaire',blank=True, null=True,)
    hierarchy = models.IntegerField(verbose_name ='Hiérachie',blank=True, null=True,)
    budget_not_provided = models.CharField(db_column='Budget-not-provided', max_length=255, blank=True, null=True,choices=BUDGETNOTAPPRO, verbose_name ='Budget non approvisé')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True, null=True)
    activity_status = models.CharField(db_column='Activity-status', max_length=255,blank=True, null=True,choices=STATUS,verbose_name ='Status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_scope = models.CharField(db_column='Activity-scope', max_length=255, blank=True, null=True,verbose_name ='Portée Activité')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_relationship = models.CharField(db_column='Type-relationship', max_length=255, blank=True, null=True,verbose_name ='Type Relation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned_start = models.DateField(db_column='Planned-start',blank=True, null=True,verbose_name ='Début Planifié')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned_end = models.DateField(db_column='Planned-end',blank=True, null=True, verbose_name ='Fin Planifiée')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_start = models.DateField(db_column='Actual-start', blank=True, null=True,verbose_name ='Début Réel')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_end = models.DateField(db_column='Actual-end',blank=True, null=True,verbose_name ='Fin Réel')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    collaboration_typeid = models.ForeignKey(CollaborationType, models.DO_NOTHING, db_column='Collaboration-typeID', blank=True, null=True,verbose_name ='Type Collaboration')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humanitarian_scopeid = models.ForeignKey(HumanitarianScope, models.DO_NOTHING, db_column='Humanitarian-scopeID', blank=True, null=True,verbose_name ='Portée Humanitaire')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tagid = models.ForeignKey(Tag, models.DO_NOTHING, db_column='tagid',blank=True, null=True,verbose_name ='Etiquette')
    default_aid_typeid = models.ForeignKey(DefaultAidType, models.DO_NOTHING, db_column='default-aid-typeID',  blank=True, null=True,verbose_name = 'Type Aide Par Defaut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_updated_datetime = models.DateField(db_column='Last-updated-datetime',blank=True, null=True,auto_now=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        verbose_name = 'Activitée'
        verbose_name_plural = 'Activitées'
    @property
    def number_of_conditions(self):
        return self.conditionid.count()
    def __str__(self):
        return '%s - %s' % (self.iati_identifier, self.title)
    

@receiver(post_save, sender=Activity, dispatch_uid="facebook_publish") 
def FacebookPublishView(sender, instance,**kwargs):
    instanceId = "40"
    clientId = "tinto.jean@openburkina.bf"
    clientSecret = "9d787b21a3164a99bdbc04a3a1461daa"
    # TODO: Customize the following 3 lines
    groupName = 'Cafdotest'  # FIXME
    groupAdmin = "22666020547"  # FIXME
    message = "Don't Sleep,Don't Sleep ,Wake up.See u to this website le http://projets-publics.openburkina.bf/projets/"  # FIXME
    headers = {
        'X-WM-CLIENT-ID': clientId, 
        'X-WM-CLIENT-SECRET': clientSecret
    }
    jsonBody = {
        'group_name': groupName,
        'group_admin': groupAdmin,
        'message': message
    }

    #r = requests.post(post_url, payload)
    r = requests.post('http://api.whatsmate.net/v3/whatsapp/group/text/message/%s' %instanceId, headers=headers, json=jsonBody)
    return Response(status=None)




class Actual(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True,verbose_name='Valeur')
    periodid = models.ForeignKey('Period', models.DO_NOTHING, db_column='periodid',verbose_name='Periode')

    class Meta:
        verbose_name='Resultat Obtenu'
    def __str__(self):
        return '%s' % (self.value)


class ActualDimension(models.Model):
    actualid = models.OneToOneField(Actual, models.DO_NOTHING, db_column='actualid', primary_key=True)
    dimensionid = models.ForeignKey('Dimension', models.DO_NOTHING, db_column='dimensionid',verbose_name='Dimension')

    class Meta:
        unique_together = (('actualid', 'dimensionid'),)
        verbose_name='Dimension Réel'


class Baseline(models.Model):
    indicatorid = models.ForeignKey('Indicator', models.DO_NOTHING, db_column='indicatorid',verbose_name='Indicateur')
    year = models.IntegerField(verbose_name ='Année')
    value = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Valeur')
    date = models.DateField(db_column='Date', blank=True, null=True,verbose_name ='Date')  # Field name made lowercase.

    class Meta:
        verbose_name='Ligne de Base'
    def __str__(self):
        return '%s' % (self.value)


class Budget(models.Model):
    activityid = models.OneToOneField(Activity, related_name='activite_budget', on_delete=models.DO_NOTHING, null=True, blank=True, db_column='activityid')
    iati_identifier = models.BigIntegerField(db_column='Iati-identifier',editable=False, null=True, blank=True)
    type = models.CharField(max_length=255,blank=True, null=True,choices=BUDGETYPE, verbose_name='Type Budget')
    statut = models.CharField(max_length=255,blank=True, null=True,choices=BUDGESTATUT, verbose_name='Statut Budget')
    period_start = models.DateField(db_column='Period-start', max_length=255, blank=True, null=True,verbose_name='Période Début')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end = models.DateField(db_column='Period-end', max_length=255, blank=True, null=True,verbose_name='Période Fin')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.FloatField(verbose_name='Montant')
    currency = models.CharField(max_length=255, blank=True, null=True,verbose_name='Dévise')
    value_date = models.DateField(db_column='Value-date', blank=True, null=True,verbose_name='Valeur Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        verbose_name = 'Budget'
        verbose_name_plural = 'Budgets'
    def __str__(self):
        return '%s - %s' % (self.value, self.currency)


class Comment(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True,verbose_name='Date')  # Field name made lowercase.
    text = models.CharField(max_length=255, blank=True, null=True,verbose_name='Texte')

    class Meta:
        verbose_name ='Commentaire'
    def __str__(self):
        return '%s - %s' % (self.date, self.text)

class DefaultAidTypeActivity(models.Model):
    default_aid_typeid = models.OneToOneField(DefaultAidType, models.DO_NOTHING, db_column='default-aid-typeID', primary_key=True,verbose_name = 'Type Aide Par Defaut')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activityid',verbose_name = 'Activité')

    class Meta:
        unique_together = (('default_aid_typeid', 'activityid'),)
        verbose_name = 'Type Aide Par Defaut'
        verbose_name_plural = 'Type Aide Par Defaut'


class Dimension(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.value)


class Indicator(models.Model):
    resultsid = models.ForeignKey('Results', models.DO_NOTHING, db_column='resultsid',verbose_name ='Resultat')
    measure = models.CharField(max_length=255, blank=True, null=True,choices=MEASURE, verbose_name ='Mesure')
    ascending = models.BooleanField(verbose_name ='Ascendant')
    aggregation_status = models.BooleanField(db_column='Aggregation-status',verbose_name ='Statut Agrégation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Titre')
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Description')
    code = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Code')

    class Meta:
        verbose_name ='Indicateur'
    def __str__(self):
        return '%s - %s' % (self.title, self.code)


class Period(models.Model):
    indicatorid = models.ForeignKey(Indicator, models.DO_NOTHING, db_column='indicatorid',verbose_name ='Indicateur')
    period_start = models.DateField(db_column='Period-start', blank=True, null=True,verbose_name ='Début Période')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end = models.DateField(db_column='Period-end', blank=True, null=True,verbose_name ='Fin période')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        verbose_name ='Periode'
    def __str__(self):
        return 'Debut %s - Fin %s' % (self.period_start, self.period_end)

class Results(models.Model):
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activityid')
    type = models.CharField(max_length=255, blank=True, null=True,choices=TYPE,verbose_name='Type')
    aggregation_status = models.BooleanField(db_column='Aggregation-status',verbose_name='Status Aggregation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, blank=True, null=True,verbose_name='Titre')
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name='Description')

    class Meta:
        verbose_name = 'Resultat'
        verbose_name_plural = 'Resultats'
    def __str__(self):
        return 'Iati identifier %s - Resultat Titre %s' % (self.activityid.iati_identifier, self.title)

class Target(models.Model):
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationid',verbose_name ='Localité')
    value = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Valeur')
    periodid = models.ForeignKey(Period, models.DO_NOTHING, db_column='periodid',verbose_name ='Periode')
    dimensionid = models.ForeignKey(Dimension, models.DO_NOTHING, db_column='dimensionid',verbose_name='Dimension')


    class Meta:
        verbose_name='Jalon'


class TargetComment2(models.Model):
    targetid = models.OneToOneField(Target, models.DO_NOTHING, db_column='targetid', primary_key=True)
    commentid = models.ForeignKey(Comment, models.DO_NOTHING, db_column='commentid', verbose_name='Commentaire')

    class Meta:
        unique_together = (('targetid', 'commentid'),)
        verbose_name = 'Commentaire Jalon'

