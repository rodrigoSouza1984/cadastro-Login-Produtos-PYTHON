from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class LoginSerializer(ModelSerializer):
    
    def authLogin(request,email, password):                   
            
        userAuthenticade = authenticate(email=email, password=password)              
         
        if userAuthenticade == None:                  
                                
            return Response({'Unauthorized': 'Dados Inválidos'}, status=status.HTTP_401_UNAUTHORIZED)
                
        else:               

            refresh = RefreshToken.for_user(userAuthenticade)    

            access_token = str(refresh.access_token)

            userCovertedDicionary = model_to_dict(userAuthenticade)

            response_data = {                   
                'user': userCovertedDicionary,             
                'access_token': access_token,
                'refreshToken': str(refresh),                    
            }

            return Response(response_data, status=status.HTTP_200_OK)

         
    def refreshToken(refresh_token):
        try:
            
            token = RefreshToken(refresh_token)
            
            token.verify()

            usuario = User.objects.get(id=token['user_id'])  

            userCovertedDicionary = model_to_dict(usuario)          

            refresh = RefreshToken.for_user(usuario)    

            access_token = str(refresh.access_token)

            response_data = {                 
                'user': userCovertedDicionary,             
                'access_token': access_token,
                'refreshToken': str(refresh),                    
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response('Refresh token Inválido ou expirado', status=status.HTTP_400_BAD_REQUEST)

                   
            


