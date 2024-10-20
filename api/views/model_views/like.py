from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from api.serializers.like import LikeSerializer, LikeReturnedSerializer
from core.models import Like, User


class LikeView(APIView):
    # permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def get(self, request):
        user = User.objects.get(id=1)

        final_data = {}

        context = {
            'user': user
        }

        likes = Like.objects.filter(liked_user=user, liked_returned=False, deleted=False)
        final_data["likes"] = LikeSerializer(likes, many=True, context=context).data

        messages = Like.objects.filter(Q(created_user=user) | Q(liked_user=user), liked_returned=True, deleted=False)
        final_data["messages"] = (LikeReturnedSerializer(messages, many=True, context=context)).data

        return Response(final_data)
