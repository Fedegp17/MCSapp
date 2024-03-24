from django.contrib import admin
from .models import BeatsPerMinute, MedicalMonitor


# Register your models here.
class BeatsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class MonitorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(BeatsPerMinute, BeatsAdmin)
admin.site.register(MedicalMonitor, MonitorAdmin)
