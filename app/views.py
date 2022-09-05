from unicodedata import category
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer, Customer_Serializer, Products_Serializer, Cart_Serializer, Orders_Serializer, Feedback_Serializer
from rest_framework.response import Response
from knox.models import AuthToken
from .models import Customer, Products, Cart, Orders, Feedback
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# Create your views here.


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class Profile_API(APIView):
    def get(self, request, format=None):
        user = self.request.user
        session = Customer.objects.filter(user=user)
        serializers = Customer_Serializer(session, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = Customer_Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            profile_details = serializers.data

            response = {
                'data': {
                    'profile_details': dict(profile_details),
                    'status': 'success',
                    'message': 'profile_details created successfully',
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Products_API(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()
        serializers = Products_Serializer(products, many=True)
        return Response(serializers.data)


class Product_API(APIView):
    def get(self, request, pk, format=None):
        product = Products.objects.get(pk=pk)
        serializers = Products_Serializer(product)
        return Response(serializers.data)


class Products_by_category1_API(APIView):
    def get(self, request, category_one, format=None):
        products = Products.filter_by_category1(category_one)
        serializers = Products_Serializer(products, many=True)
        return Response(serializers.data)


class Products_by_category2_API(APIView):
    def get(self, request, category_two, format=None):
        products = Products.filter_by_category2(category_two)
        serializers = Products_Serializer(products, many=True)
        return Response(serializers.data)

# def location(request, location):
#     images = Image.filter_by_location(location)
#     print(images)
#     title = "Location"
#     return render(request, 'location.html', {'location_images': images, "title":title})


class Cart_API(APIView):
    def get(self, request, format=None):
        user = self.request.user
        cart = Cart.objects.filter(user=user)
        serializers = Cart_Serializer(cart, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = Cart_Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            cart_details = serializers.data

            response = {
                'data': {
                    'cart_details': dict(cart_details),
                    'status': 'success',
                    'message': 'cart_details created successfully',
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Orders_API(APIView):
    def get(self, request, format=None):
        user = self.request.user
        orders = Orders.objects.filter(user=user)
        serializers = Orders_Serializer(orders, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = Orders_Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            order_details = serializers.data

            response = {
                'data': {
                    'order_details': dict(order_details),
                    'status': 'success',
                    'message': 'order_details created successfully',
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_order_details(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            return Http404()

    def put(self, request, pk, format=None):
        order_details = self.get_order_details(pk)
        serializers = Orders_Serializer(order_details, request.data)
        if serializers.is_valid():
            serializers.save()
            order_details = serializers.data
            response = {
                'data': {
                    'order_details': dict(order_details),
                    'status': 'success',
                    'message': 'order_details updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class Feedback_API(APIView):
    def post(self, request, format=None):
        serializers = Feedback_Serializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            feedback_details = serializers.data

            response = {
                'data': {
                    'feedback_details': dict(feedback_details),
                    'status': 'success',
                    'message': 'feedback_details created successfully',
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
