from django.apps import AppConfig


class IotcloudConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'IoTCloud'
    # The verbose name is used to change the 'visualization' name in the admin tab
    verbose_name = 'Hospitales'
