from rest_framework import generics
from rest_framework import response
from rest_framework import status
from .serializers import RegistrationSerializer


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"email": serializer.validated_data("email")}
            return response(data, status=status.HTTP_201_CREATED)
