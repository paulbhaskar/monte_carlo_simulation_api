from rest_framework_mongoengine import serializers

from monte_carlo_simulation.models import Trial


class TrialSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Trial
        fields = '__all__'
