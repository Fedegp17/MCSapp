from django.contrib import admin
from .models import Hospital, Medico, Paciente


# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class MedicoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PacienteAdmin(admin.ModelAdmin):
    readonly_fields = ('ingreso', 'updated')


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
