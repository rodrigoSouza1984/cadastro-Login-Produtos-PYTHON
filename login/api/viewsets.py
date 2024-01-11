from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from login.api.serializers import AuthSerializer
from rest_framework.response import Response
from rest_framework import status


class LoginViewSet(ModelViewSet):    
    serializer_class = AuthSerializer
    
# @api_view(['POST'])
# def authLogin(request):
#     if request.method == 'POST':        

#         email = request.data.get('email')
#         password = request.data.get('password')        

#         if email and password:
#             return AuthSerializer.authLogin(request,email,password)
#         else:
#             return Response({'Bad Request':'enviar email e password'}, status=status.HTTP_400_BAD_REQUEST)


        


   