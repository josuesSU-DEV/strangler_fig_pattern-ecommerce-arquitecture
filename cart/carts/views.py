from rest_framework import generics
from rest_framework.response import Response
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer, CartItemSerializer


class CartAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ShowCartAPIView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, usuario=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
