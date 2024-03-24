from rest_framework import serializers
from .models import BeatsPerMinute


class BeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeatsPerMinute
        fields = ('beats', 'created', 'updated')
        # fields = '__all__' with this we can pull all the fields, including the ID
