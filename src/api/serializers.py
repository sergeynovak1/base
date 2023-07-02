from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'email', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
