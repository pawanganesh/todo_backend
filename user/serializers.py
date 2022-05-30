from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate

from utils.password import validate_password

USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ['full_name', 'email']


class UserRegistrationRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration request
    """
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)

    class Meta:
        model = USER
        fields = ('full_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    @staticmethod
    def validate_password(value):
        errors = validate_password(value)
        if errors:
            raise serializers.ValidationError(errors)
        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email = attrs.get('email')
        if not email:
            raise serializers.ValidationError('Email is required')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = USER(**validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user


class UserLoginRequestSerializer(serializers.Serializer):
    """
    Serializer for user login request
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128, required=True, write_only=True)
    user = serializers.ReadOnlyField

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError({'message': 'Invalid credentials'})
        attrs['user'] = user
        return attrs
