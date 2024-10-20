from django.db.models import Q
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from django.core.exceptions import ObjectDoesNotExist

from core.models import Like, Message


# A serializer specifically for the case where a user has liked you, but you haven't liked them back
class LikeSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(source="created_user.uid", read_only=True)
    display_name = serializers.CharField(source="created_user.display_name", read_only=True)
    prof_image = serializers.CharField(source="created_user.prof_image", read_only=True)

    class Meta:
        model = Like
        fields = ['uid', 'display_name', 'prof_image']


# Return all likes for the message pane, so any like the user has been involved in and was returned
class LikeReturnedSerializer(serializers.ModelSerializer):
    uid = SerializerMethodField(method_name='get_uid', read_only=True)
    display_name = SerializerMethodField(method_name='get_name', read_only=True)
    prof_image = SerializerMethodField(method_name='get_image', read_only=True)
    last_message = SerializerMethodField(method_name='get_message', read_only=True)

    def get_uid(self, like):
        user = self.context.get("user")

        return like.created_user.uid if user == like.liked_user else like.liked_user.uid

    def get_name(self, like):
        user = self.context.get("user")

        return like.created_user.display_name if user == like.liked_user else like.liked_user.display_name

    def get_image(self, like):
        user = self.context.get("user")

        return like.created_user.prof_image.name if user == like.liked_user else like.liked_user.prof_image.name

    def get_message(self, like):
        messages = Message.objects.filter(
            (Q(sent_user=like.created_user) & Q(received_user=like.liked_user)) |
            (Q(sent_user=like.liked_user) & Q(received_user=like.created_user)),
        )

        result = ""
        try:
            result = messages.latest("created_date").message
        except ObjectDoesNotExist:
            result = "No messages yet"

        return result

    class Meta:
        model = Like
        fields = ['uid', 'display_name', 'prof_image', 'last_message']
