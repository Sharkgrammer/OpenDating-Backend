from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.models import Like


# A serializer specifically for the case where a user has liked you, but you haven't liked them back
class LikeSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source="created_user.full_name", read_only=True)
    prof_image = serializers.CharField(source="created_user.prof_image", read_only=True)

    class Meta:
        model = Like
        fields = ['display_name', 'prof_image']


class LikeReturnedSerializer(serializers.ModelSerializer):
    display_name = SerializerMethodField(method_name='get_name', read_only=True)
    prof_image = SerializerMethodField(method_name='get_image', read_only=True)

    def get_name(self, like):
        user = self.context.get("user")

        return like.created_user.display_name if user == like.liked_user else like.liked_user.display_name

    def get_image(self, like):
        user = self.context.get("user")

        return like.created_user.prof_image.name if user == like.liked_user else like.liked_user.prof_image.name

    class Meta:
        model = Like
        fields = ['display_name', 'prof_image']
