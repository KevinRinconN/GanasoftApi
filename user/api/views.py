from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.api.serializers import UserRegistrerSerializer


class RegistrerView(APIView):
    # def post(self, request):
    #     print('registrando usuario...')
    #     return Response(status=status.HTTP_200_OK, data='todo ok')
    
    def post(self, request):        
        serializer = UserRegistrerSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)