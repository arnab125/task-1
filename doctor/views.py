from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from .models import Doctor
from .serializers import DoctorSerializer



def check_credentials(username, password):
    try:
        user = Doctor.objects.get(username=username)
    except Doctor.DoesNotExist:
        return None
    if user.check_password(password):
        return user
    return None

@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = check_credentials(username, password)
    if user is not None:
        login(request, user)
        return Response({'username': user.username}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def doctor_info(request, username):
    try:
        doctor = Doctor.objects.get(username=username)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data)
