from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    profile_pic = serializers.ImageField(required=False)
    line1 = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    pincode = serializers.CharField()

    class Meta:
        model = Patient
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'profile_pic', 'line1', 'city', 'state', 'pincode')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Patient.objects.create_user(password=password, **validated_data)
        return user
