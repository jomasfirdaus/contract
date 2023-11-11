from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from contract.models import *
from import_export import resources

# Register your models here.

class ContractTypeResource(resources.ModelResource):
    class Meta:
        model = ContractType
class ContractTypeAdmin(ImportExportModelAdmin):
    resource_class = ContractTypeResource
admin.site.register(ContractType, ContractTypeAdmin)

class ContractResource(resources.ModelResource):
    class Meta:
        model = Contract
class ContractAdmin(ImportExportModelAdmin):
    resource_class = ContractResource
admin.site.register(Contract, ContractAdmin)