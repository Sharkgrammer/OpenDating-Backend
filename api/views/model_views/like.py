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

        returned = request.GET.get("returned", False)

        user = User.objects.get(id=1)
        serializer = None
        context = {
            'user': user
        }

        if returned:
            data = Like.objects.filter(Q(created_user=user) | Q(liked_user=user), liked_returned=True, deleted=False)

            serializer = LikeReturnedSerializer(data, many=True, context=context)
        else:
            data = Like.objects.all()

            serializer = LikeSerializer(data, many=True, context=context)

        return Response(serializer.data)
