from django.contrib import admin
from .models import *
# Register your models here.
class ResponsiblePersonsInline(admin.TabularInline):
    model = ResponsiblePersons
    extra = 3
class LicenceInline(admin.StackedInline):
    model = Licence
    extra = 1
class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Public data',               {'fields': ['company_n','address']}),
        ('Special Information', {'fields': ['registration','specification','owner_id','responpers_id'], 'classes': ['collapse']}),
    ]
    inlines = [LicenceInline]
    list_display = ('company_n', 'address', 'specification')
    list_filter = ['company_n']
    search_fields = ['company_n']

#admin.site.register(Licence)
admin.site.register(ResponsiblePersons)
admin.site.register(Owner)
admin.site.register(Company,CompanyAdmin)
