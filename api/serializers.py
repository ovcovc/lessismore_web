from rest_framework import serializers
from injuries.models import Injury

__author__ = 'piotrolejnik88'


class InjurySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Injury
        fields = ('name', 'description', 'created_at', 'x_axis', 'y_axis', 'exercises', 'treatments', 'recovery_time',
                  'medication')