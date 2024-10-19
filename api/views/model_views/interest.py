from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.interest_cat import InterestCategorySerializer
from core.models import InterestCategory


class InterestView(APIView):
    #permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def get(self, request):
        # Get all interests
        data = InterestCategory.objects.all()

        # user_data = user_data.prefetch_related("images")

        serializer = InterestCategorySerializer(data, many=True)

        return Response(serializer.data)
