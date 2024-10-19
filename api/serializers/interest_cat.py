from rest_framework import serializers
from core.models import InterestCategory


class InterestCategorySerializer(serializers.ModelSerializer):
    interests = serializers.StringRelatedField(many=True)

    class Meta:
        model = InterestCategory
        fields = ['title', 'interests']
