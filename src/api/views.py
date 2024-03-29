from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .serializers import UserSerializer
from users.models import User


class UserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer,)

    def get(self, request, id=None, *args, **kwargs):
        role_filter = request.GET.get('role')
        search_query = request.GET.get('search')
        queryset = User.objects.all()

        if search_query:
            queryset = queryset.filter(Q(username__icontains=search_query) | Q(email__icontains=search_query))

        if role_filter:
            queryset = queryset.filter(role=role_filter)

        if id is not None:
            queryset = queryset.filter(id=id)

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

    def delete(self, request, *args, **kwargs):
        id = self.kwargs["id"]
        queryset = User.objects.filter(id=id)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)


@csrf_exempt
def get_method(request):
    return HttpResponse("Ответ для GET запроса")


@csrf_exempt
def post_method(request):
    return HttpResponse("Ответ для POST запроса")

