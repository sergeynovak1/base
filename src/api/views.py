from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from .serializers import UserSerializer
from users.models import User


class UserView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer,)

    def get(self, request, id=None, *args, **kwargs):
        queryset = User.objects.filter(id=id) if id else User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        return Response(UserSerializer(user_obj).data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        id = self.kwargs["id"]
        user_obj = User.objects.filter(id=id).first()
        if not user_obj:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user_obj = serializer.save()
        return Response(UserSerializer(updated_user_obj).data, status=status.HTTP_200_OK)
