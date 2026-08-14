from django.contrib.auth import authenticate
from rest_framework import generics, serializers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import RegisterSerializer

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        token, created = Token.objects.get_or_create(user=user)

        return {
            'token': token.key,
            'username': user.username
        }


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/entries/')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if not username or not password:
            return render(
                request,
                'register.html',
                {'error': 'Username and password are required.'}
            )

        if password != password2:
            return render(
                request,
                'register.html',
                {'error': 'Passwords do not match.'}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'register.html',
                {'error': 'Username already exists.'}
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('/entries/')

    return render(request, 'register.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/entries/')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('/entries/')

        return render(
            request,
            'login.html',
            {'error': 'Invalid username or password.'}
        )

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/')