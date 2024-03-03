from django.db import models

"""When creating or updating a model for an app, 2 commands are esential here:
   python manage.py makemigrations 'app name'   and 
   python manage.py migrate 'app name'  
   
   this commands will modify the DataBase by updating the existing models, or creating the new models, if this 
   commands are not executed, the changes will make no effect in the server and the DataBase 
   
   ERROR warnings: 
   If the database has already information, and we modify the models, we will probably see the following error:
   
   'It is impossible to add a non-nullable field 'class example name' to feature without specifying a default. This is 
   because the database needs something to populate existing rows.'
   
   In this case we have 2 options, set a default value, default=''
   Or
   Delete the migration data files, in the 'migrations' file of the app, (DO NOT DELETE THE __init__.py file). However,
   this solution will erase our current data, therefore we need to be cautious about this.
   """


# Create your models here.
# Model used for saving a hospital in the DataBase
class Hospital(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    address = models.TextField(max_length=300, verbose_name="Dirección")
    image = models.ImageField(verbose_name="Logo del hospital", null=True, blank=True)
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitales"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.name


class Medico(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellidopaterno = models.CharField(max_length=30, verbose_name='Apellido paterno')
    apellidomaterno = models.CharField(max_length=30, verbose_name='Apellido materno')
    especialidad = models.CharField(max_length=40, verbose_name='Especialidad médica')
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    apellidopaterno = models.CharField(max_length=30, verbose_name='Apellido paterno')
    apellidomaterno = models.CharField(max_length=30, verbose_name='Apellido materno')
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de ingreso")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["-ingreso"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.nombre

