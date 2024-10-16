from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

from ..Model.CustomUser import CustomUser
from ..Serializer.UserSerializer import UserSerializer


class UserView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        pk = self.kwargs.get('pk')
        email = self.kwargs.get('email')

        if pk is not None:
            try:
                return self.queryset.get(pk=pk)
            except CustomUser.DoesNotExist:
                raise NotFound('User with this primary key doesnt\' exists.')

        if email is not None:
            try:
                return self.queryset.get(email=email)
            except CustomUser.DoesNotExist:
                raise NotFound("User with this email doesn't exist.")

        raise NotFound("User not found")

    @action(detail=False, methods=['post'])
    def login(self, request):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."})

        user = authenticate(username=username, password=password)

        if user is None:
            print(f"Authentication failed for user: {username}")
            return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        if request.user is None:
            return Response({"error": "User is not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            token = Token.objects.get(user=request.user)
            token.delete()

            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)

        except Token.DoesNotExist:
            return Response({"error": "No token found for the user."}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "message": "User registered successfully.",
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
