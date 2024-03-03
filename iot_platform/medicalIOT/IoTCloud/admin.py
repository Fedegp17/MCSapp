from django.contrib import admin
from .models import Hospital


# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Hospital, HospitalAdmin)
