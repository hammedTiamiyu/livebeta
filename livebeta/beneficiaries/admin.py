from django.contrib import admin
from .models import Beneficiary

# Register your models here.
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date")
admin.site.register(Beneficiary, BeneficiaryAdmin)

