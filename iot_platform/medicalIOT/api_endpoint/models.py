from django.db import models


# Create your models here.
class BeatsPerMinute(models.Model):  # PulseOximeter Database
    beats = models.FloatField(verbose_name='Latidos por minuto')
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Pulsioximetro"
        verbose_name_plural = "Pulsioximetro"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we personalize the object or register title in the admin tab
    def __str__(self):
        titulo = str(self.beats)
        fecha = str(self.created)
        return f'{titulo} registrado en {fecha}'


class MedicalMonitor(models.Model):  # Medical Monitor Database
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    heart_rate = models.FloatField(verbose_name='Ritmo cardiaco')
    spo2 = models.FloatField(verbose_name='Saturación de oxígeno')
    respiracion = models.FloatField(verbose_name='Respiraciones por minuto')
    presion_sistolica = models.FloatField(verbose_name='Presión sistólica')
    presion_diastolica = models.FloatField(verbose_name='Presión diastolica')
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Signos vitales"
        verbose_name_plural = "Signos vitales"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we personalize the object or register title in the admin tab
    def __str__(self):
        nombre = self.nombre
        fecha = str(self.created)
        return f'Signos vitales de {nombre} en {fecha}'




