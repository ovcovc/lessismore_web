from rest_framework import serializers
from injuries.models import Injury

__author__ = 'piotrolejnik88'


class InjurySerializer(serializers.ModelSerializer):

    class Meta:
        model = Injury
        fields = ('id', 'name', 'description', 'created_at', 'x_axis', 'y_axis', 'exercises', 'treatments',
                  'recovery_time', 'medication', 'is_accepted')

    def create(self, validated_data):
        injury = Injury(name = validated_data['name'], description=validated_data['description'],
                        x_axis=validated_data['x_axis'], y_axis=validated_data['y_axis'],
                        exercises=validated_data['exercises'], treatments=validated_data['treatments'],
                        recovery_time=validated_data['recovery_time'], medication=validated_data['medication'])
        injury.save()
        return validated_data