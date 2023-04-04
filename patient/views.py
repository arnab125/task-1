from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from .models import Patient
from .serializers import PatientSerializer


def check_credentials(username, password):
    try:
        user = Patient.objects.get(username=username)
    except Patient.DoesNotExist:
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
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def patient_info(request, username):
    try:
        patient = Patient.objects.get(username=username)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)
