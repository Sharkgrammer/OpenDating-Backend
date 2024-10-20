from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.stat import StatSerializer
from core.models import User, Stat


class StatView(APIView):
    # permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def get(self, request):
        user = request.user

        # We assume that the stat model already exists

        data = Stat.objects.get(user=user)
        serializer = StatSerializer(data)

        return Response(serializer.data)
