from rest_framework import generics
from rest_framework.response import Response
from .serializers import ContactMessageSerializer


class SendMessageAPIView(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"mensaje": "Mensaje enviado con éxito"})
