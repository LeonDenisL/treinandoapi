from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Oficio
from .serializers import OficioSerializer

class OficioAPIView(APIView):
    """
    Oficio PM
    """
    def get(self, request):
        oficios = Oficio.objects.all()
        serializer = OficioSerializer(oficios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OficioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



