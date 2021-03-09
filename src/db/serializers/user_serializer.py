from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    password = serializers.CharField

    def create(self, validated_data):
        # django auto hashes passwords
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

