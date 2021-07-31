from rest_framework import serializers    
from .models import UserModel
from django.views.decorators.cache import never_cache

@never_cache


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username"]
        