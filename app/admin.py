from django.contrib import admin
from .models import (
    Scholarship,
    Applicant,
    Application,
    Document,
    Evaluation,
    Beneficiary
)


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'allowance', 'slots', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Financial Details', {
            'fields': ('allowance', 'slots')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'contact_no', 'birthdate', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'contact_no')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'birthdate')
        }),
        ('Contact Information', {
            'fields': ('email', 'contact_no', 'address')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class EvaluationInline(admin.TabularInline):
    model = Evaluation
    extra = 0
    fields = ('evaluator', 'score', 'remarks', 'eval_date')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'applicant', 'scholarship', 'status', 'date_applied', 'created_at')
    list_filter = ('status', 'date_applied', 'created_at', 'scholarship')
    search_fields = ('applicant__first_name', 'applicant__last_name', 'scholarship__name')
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ['applicant', 'scholarship']
    inlines = [EvaluationInline]
    fieldsets = (
        ('Application Details', {
            'fields': ('applicant', 'scholarship', 'date_applied')
        }),
        ('Status', {
            'fields': ('status', 'remarks')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_type', 'applicant', 'uploaded_at', 'file_path')
    list_filter = ('doc_type', 'uploaded_at')
    search_fields = ('applicant__first_name', 'applicant__last_name', 'doc_type')
    readonly_fields = ('uploaded_at',)
    autocomplete_fields = ['applicant']
    fieldsets = (
        ('Document Information', {
            'fields': ('applicant', 'doc_type', 'file_path')
        }),
        ('Additional Details', {
            'fields': ('notes', 'uploaded_at')
        }),
    )


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('application', 'evaluator', 'score', 'eval_date')
    list_filter = ('eval_date', 'evaluator')
    search_fields = ('application__applicant__first_name', 'application__applicant__last_name', 'evaluator')
    readonly_fields = ('eval_date',)
    autocomplete_fields = ['application']
    fieldsets = (
        ('Evaluation Details', {
            'fields': ('application', 'evaluator', 'score')
        }),
        ('Comments', {
            'fields': ('remarks', 'eval_date')
        }),
    )


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'scholarship', 'status', 'awarded_date')
    list_filter = ('status', 'awarded_date', 'scholarship')
    search_fields = ('applicant__first_name', 'applicant__last_name', 'scholarship__name')
    autocomplete_fields = ['applicant', 'scholarship']
    fieldsets = (
        ('Beneficiary Information', {
            'fields': ('applicant', 'scholarship', 'awarded_date')
        }),
        ('Status', {
            'fields': ('status', 'notes')
        }),
    )