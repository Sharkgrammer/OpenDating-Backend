from rest_framework import serializers
from core.models import Stat


class StatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stat
        fields = ['likes', 'dislikes', 'days_on', 'top_interests']
