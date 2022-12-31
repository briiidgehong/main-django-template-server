from django.contrib.auth import login, logout
from rest_framework import views, viewsets, permissions, generics, response
from django.contrib.auth import get_user_model
from users.serializers import UsersSerializer, LoginSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from drf_yasg.utils import swagger_auto_schema

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    swagger_tags = ["USERS"]
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SessionLoginView(views.APIView):
    swagger_tags = ["SESSION"]    
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(operation_id="세션로그인")
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UsersSerializer(user).data)


class SessionLogoutView(views.APIView):
    swagger_tags = ["SESSION"]
    @swagger_auto_schema(operation_id="세션로그아웃")
    def post(self, request):
        logout(request)
        return response.Response()


class RegisterView(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(operation_id="회원가입")
    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)