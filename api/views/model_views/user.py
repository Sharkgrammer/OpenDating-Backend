from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.user import UserGetSerializer
from core.functions.gen_functions import get_today
from core.models import User


class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def get(self, request):

        uid = request.GET.get("uid", None)
        login = request.GET.get("login", False)

        user = request.user
        user_data = []
        context = {}

        if uid is None:
            # User has requested their own data
            if login:
                user.last_login = get_today()
                user.save()

            user_data = user

        else:
            user_data = User.objects.get(uid=uid)
            context["exclude_fields"] = ["date_joined", "email", "full_name"]

        # user_data = user_data.prefetch_related("images")

        serializer = UserGetSerializer(user_data, context=context)

        return Response(serializer.data)
