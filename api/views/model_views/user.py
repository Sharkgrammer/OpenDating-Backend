from django.http import HttpResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.user import UserGetSerializer
from core.models import User


class UserView(APIView):
    # permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def get(self, request):
        users = User.objects.prefetch_related("images")

        serializer = UserGetSerializer(users, many=True)

        return Response(serializer.data)
