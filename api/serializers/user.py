from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.models import User


class UserGetSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    rating = SerializerMethodField(method_name='get_rating', read_only=True)

    def get_rating(self, user):
        access_user = self.context.get("user")

        # TODO remove temp code as this situation should never happen
        if access_user is not None and access_user == user:
            return "90"

        # TODO, use interests to gauge rating
        return "0"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        exclude_fields = self.context.get('exclude_fields', [])

        for field in exclude_fields:
            representation.pop(field)

        return representation

    class Meta:
        model = User
        fields = ['uid', 'display_name', 'description', 'last_login', 'images', 'email', 'full_name', 'date_joined',
                  'interests', 'age', 'rating']
