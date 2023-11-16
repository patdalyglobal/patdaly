from django.contrib import admin
from .forms import ProjectForm
from .models import ContactMessage, Contractor, Supervisor, Project

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    search_fields = ('full_name', 'email', 'subject')
    list_filter = ('created_at',)

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'rc_number')
    search_fields = ('name', 'phone_number', 'rc_number')

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'id_number')
    search_fields = ('name', 'department', 'id_number')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    #form = ProjectForm
    list_display = ('name', 'code', 'location', 'date_awarded', 'date_contract_reviewed', 'formatted_contract_sum', 'formatted_revised_contract_sum', 'completion_status', 'contractor', 'supervisor')
    search_fields = ('name', 'code', 'location')
    list_filter = ('date_awarded', 'date_contract_reviewed', 'completion_status')

