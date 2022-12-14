from .models import User, Customer, Products, Orders, Cart, Feedback, Category_One, Category_Two
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    confirmPassword = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirmPassword'
                  )
        # extra_kwargs = {
        #   'first_name': {'required': True},
        #   'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirmPassword']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')


# class Today_Serializer(serializers.ModelSerializer):
#     users = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = Today_Deals
#         fields = "__all__"


# class Recommended_Serializer(serializers.ModelSerializer):
#     users = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = Recommended_Products
#         fields = "__all__"


class Customer_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"


class Products_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = "__all__"


# class Similar_Serializer(serializers.ModelSerializer):
#     users = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = Similar_Products
#         fields = "__all__"


class Cart_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"


class Orders_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"


class Feedback_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Feedback
        fields = "__all__"


class Category1_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Category_One
        fields = "__all__"


class Category2_Serializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Category_Two
        fields = "__all__"
