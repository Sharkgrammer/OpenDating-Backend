from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.user import UserGetSerializer


@api_view(['GET'])
@action(detail=True, permission_classes=[IsAuthenticated])
def get_feed(request):
    user = request.user

    context = {
        "user": user
    }

    serializer = UserGetSerializer(user, context=context)

    return Response(serializer.data)
