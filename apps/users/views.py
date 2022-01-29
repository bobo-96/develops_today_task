from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from apps.users.models import User
from apps.users.permissions import IsUserOwnerOrReadOnly
from apps.users.serializers import RegisterSerializer, UserSerializer


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOwnerOrReadOnly,)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
