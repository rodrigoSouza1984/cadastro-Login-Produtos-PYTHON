from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from login.api.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class LoginViewSet(ModelViewSet):    
    serializer_class = LoginSerializer
    
@api_view(['POST'])
def authLogin(request):
    if request.method == 'POST':        

        email = request.data.get('email')
        password = request.data.get('password')        

        if email and password:
            return LoginSerializer.authLogin(request,email,password)
        else:
            return Response({'Bad Request':'enviar email e password'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def refreshLogin(request):
    if request.method == 'POST':        

        refresh = request.data.get('refresh')
               

        if refresh: 
            return LoginSerializer.refreshToken(refresh)
        else:
            return Response({'Bad Request':'enviar email e password'}, status=status.HTTP_400_BAD_REQUEST)
        



        


   