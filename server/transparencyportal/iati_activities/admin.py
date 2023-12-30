from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


from iati_activities.models import Activity, \
        ActivityParticipatingOrg, ActualDimension, \
        Actual, ActualDocumentLink, Baseline, Budget, BaselineDocumentLink, Comment, \
        ContactInfo, Dimension, DocumentLink, DocumentLinkIndicator, DocumentLinkResults, Indicator, Period, PlannedDisbursement,  \
        Results, Target, TargetComment2, Transaction,DefaultAidTypeActivity, \
        DefaultFinanceTypeActivity


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

class DefaultAidTypeActivityline(admin.StackedInline):
    model = DefaultAidTypeActivity
    extra = 0

class DefaultFinanceTypeActivityline(admin.StackedInline):
    model = DefaultFinanceTypeActivity
    extra = 0

class ActivityParticipatingOrgline(admin.StackedInline):
    model = ActivityParticipatingOrg
    extra = 0

class Resultsline(admin.TabularInline):
    model = Results

    extra = 0

class Budgetline(admin.StackedInline):
    model = Budget
    extra = 0

class Transactionline(admin.StackedInline):
    model = Transaction
    extra = 0

class Contactline(admin.StackedInline):
    model = ContactInfo
    extra = 0

@admin.register(Activity)
class ActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('regionid3','countryid3','locationid','iati_identifier')
    list_filter = ('humanitarian','regionid3','countryid3','iati_identifier')
    list_per_page=10
    inlines = [
             Budgetline, ActivityParticipatingOrgline,\
             Resultsline, DefaultFinanceTypeActivityline, \
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
        TargetComment2line
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
    list_display = ('activityid','organizationid2','organizationid','sectorid','ref','transaction_type','transaction_date','value','currency')
    search_fields = ('activityid','organizationid2','organizationid','sectorid','ref','transaction_type','transaction_date','value','currency')
    list_filter = ('activityid','organizationid2','organizationid','sectorid','ref','transaction_type','transaction_date','value','currency')
    list_per_page=10

@admin.register(Results)
class ResultsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
     list_display = ('activityid','type','aggregation_status','title','description')
     search_fields = ('activityid','type','aggregation_status','title','description')
     list_filter = ('activityid','type','aggregation_status','title','description')
     list_per_page=10

@admin.register(Budget)
class ActivityBudgetAdmin(ImportExportModelAdmin, admin.ModelAdmin):
     list_display = ('activityid','type','statut','period_start','period_end','value','currency','value_date')
     search_fields = ('activityid','type','statut','period_start','period_end','value','currency','value_date')
     list_filter = ('activityid','type','statut','period_start','period_end','value','currency','value_date')
     list_per_page=10

@admin.register(ActivityParticipatingOrg)
class ActivityActivityParticipatingOrgAdmin(ImportExportModelAdmin, admin.ModelAdmin):
     list_display = ('activityid','organizationid','role')
     search_fields = ('activityid','role')
     list_filter = ('activityid','role')
     list_per_page=10
