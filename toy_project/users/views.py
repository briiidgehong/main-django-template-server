from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from users.serializers import UsersSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    swagger_tags = ["USERS"]
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [JWTAuthentication]