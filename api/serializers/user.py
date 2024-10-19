from rest_framework import serializers
from core.models import User


class UserGetSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['uid', 'display_name', 'description', 'last_login', 'images']
