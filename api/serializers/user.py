from rest_framework import serializers
from core.models import User


class UserGetSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        exclude_fields = self.context.get('exclude_fields', [])

        for field in exclude_fields:
            representation.pop(field)

        return representation

    class Meta:
        model = User
        fields = ['uid', 'display_name', 'description', 'last_login', 'images', 'email', 'full_name', 'date_joined']
