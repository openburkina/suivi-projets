from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


from iati_activities.models import Activity,ActivityCollaborationType,ActivityDate,ActivityHumanitarianScope, \
    ActivityLocation, ActivityOrganization, ActivityParticipatingOrg, ActivitySector, ActivityTag, ActualDimension, \
        Actual, ActualDocumentLink, Baseline, Budget, BaselineDocumentLink, Comment, ConditionActivity, \
        ContactInfo, Dimension, DocumentLink, DocumentLinkIndicator, DocumentLinkResults, Indicator, Period, PlannedDisbursement,  \
        Results, Target, TargetComment2, TargetDimension, Transaction, TransactionSector,DefaultAidTypeActivity, \
        DefaultFinanceTypeActivity

class ActivityRessouces(resources.ModelResource):
    class Meta:
        model = ActivityOrganization
        fields = ('activityid','organizationid','activityid__regionid3','activityid__countryid3','activityid__activityid','activityid__contact_infoid','activityid__last_updated_datetime','activityid__lang','activityid__default_currency',
        'activityid__humanitarian','activityid__hierarchy','activityid__budget_not_provided','activityid__iati_identifier','activityid__title','activityid__description','activityid__activity_status','activityid__activity_scope',
        'activityid__type_relationship','activityid__transaction__organizationid2')

class Actualline(admin.StackedInline):
    model = Actual
    extra = 0

class ActualDocumentLinkline(admin.StackedInline):
    model = ActualDocumentLink
    extra = 0

class Baselineline(admin.StackedInline):
    model = Baseline
    extra = 0

class BaselineDocumentLinkline(admin.StackedInline):
    model = BaselineDocumentLink
    extra = 0

class Commentline(admin.StackedInline):
    model = Comment
    extra = 0

class ActualDimensionline(admin.StackedInline):
    model = ActualDimension

class Dimensionline(admin.StackedInline):
    model = Dimension
    extra = 0

class DocumentLinkline(admin.StackedInline):
    model = DocumentLink
    extra = 0

class DocumentLinkIndicatorline(admin.StackedInline):
    model = DocumentLinkIndicator
    extra = 0

class DocumentLinkResultsline(admin.StackedInline):
    model = DocumentLinkResults
    extra = 0

class Indicatorline(admin.TabularInline):
    model = Indicator
    extra = 0

class Periodline(admin.StackedInline):
    model = Period
    extra = 0

class Targetline(admin.StackedInline):
    model = Target
    extra = 0

class PlannedDisbursementline(admin.StackedInline):
    model = PlannedDisbursement
    extra = 0

class TargetComment2line(admin.StackedInline):
    model = TargetComment2
    extra = 0

class TargetDimensionline(admin.StackedInline):
    model = TargetDimension
    extra = 0

class DefaultAidTypeActivityline(admin.StackedInline):
    model = DefaultAidTypeActivity
    extra = 0

class DefaultFinanceTypeActivityline(admin.StackedInline):
    model = DefaultFinanceTypeActivity
    extra = 0

class ActivityCollaborationTypeline(admin.StackedInline):
    model = ActivityCollaborationType
    extra = 0

class ActivityHumanitarianScopeline(admin.StackedInline):
    model = ActivityHumanitarianScope
    extra = 0

class ActivityParticipatingOrgline(admin.StackedInline):
    model = ActivityParticipatingOrg
    extra = 0

class ActivitySectorline(admin.StackedInline):
    model = ActivitySector
    extra = 2

class ActivityDateline(admin.StackedInline):
    model = ActivityDate
    extra = 0

class ActivityLocationline(admin.StackedInline):
    model = ActivityLocation
    extra = 0

class Resultsline(admin.TabularInline):
    model = Results

    extra = 0


class ActivityOrganizationline(admin.StackedInline):
    model = ActivityOrganization
    extra = 0

class ActivityTagline(admin.StackedInline):
    model = ActivityTag
    extra = 0

class Budgetline(admin.StackedInline):
    model = Budget
    extra = 0

class ConditionActivityline(admin.StackedInline):
    model = ConditionActivity
    extra = 0

class TransactionSectorline(admin.StackedInline):
    model = TransactionSector
    extra = 0

class Transactionline(admin.StackedInline):
    model = Transaction
    extra = 0

class Contactline(admin.StackedInline):
    model = ContactInfo
    extra = 0

@admin.register(Activity)
class ActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [ActivityRessouces]
    list_display = ('iati_identifier','title','regionid3','countryid3','humanitarian')
    search_fields = ('regionid3','countryid3','iati_identifier')
    list_filter = ('humanitarian','regionid3','countryid3','iati_identifier')
    list_per_page=10
    inlines = [
        ActivityLocationline, ActivitySectorline, ActivityOrganizationline, Budgetline, ActivityTagline, ActivityParticipatingOrgline, ActivityDateline,\
             Resultsline, ActivityCollaborationTypeline, ActivityHumanitarianScopeline, ConditionActivityline, DefaultFinanceTypeActivityline, \
                DefaultAidTypeActivityline, DocumentLinkline, PlannedDisbursementline
    ]

@admin.register(Indicator)
class IndicatorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('measure','title','description','code','ascending')
    search_fields = ('measure','title')
    list_filter = ('measure','title','code','ascending')
    list_per_page=10
    inlines = [
        Periodline, DocumentLinkIndicatorline,Baselineline
    ]

@admin.register(Target)
class TargetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('locationid','value','periodid')
    search_fields = ('locationid','value')
    list_filter = ('locationid','value')
    list_per_page=10
    inlines = [
        TargetComment2line, TargetDimensionline
    ]

@admin.register(Actual)
class ActualAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('value','periodid')
    search_fields = ('periodid','value')
    list_filter = ('periodid','value')
    list_per_page=10
    inlines = [
        ActualDimensionline, ActualDocumentLinkline
    ]

@admin.register(Transaction)
class TransactionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('activityid','organizationid2','organizationid','ref','transaction_type','transaction_date','value','currency')
    search_fields = ('activityid','organizationid2','organizationid','ref','transaction_type','transaction_date','value','currency')
    list_filter = ('activityid','organizationid2','organizationid','ref','transaction_type','transaction_date','value','currency')
    list_per_page=10
    inlines = [
        TransactionSectorline
    ]
