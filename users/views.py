from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView

# Create your views here.

class UserView(APIView):
     def get(self, request):
         serializer = UserSerializer(request.user)
         return Response(serializer.data)
