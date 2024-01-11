from rest_framework.serializers import ModelSerializer
from user.api.serializers import UserSerializer
serializer_class = UserSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.hashers import check_password
#from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User

from django.forms.models import model_to_dict
from datetime import datetime

from django.contrib.auth import authenticate


#import jwt
import datetime

class LoginSerializer(ModelSerializer):
    
    def aa():
        return True
    # def authLogin(request,email, password):
    #     if email:                    

    #         try:                                  
    #             user = User.objects.get(email=email)                                      
    #         except:
    #             return Response({'Unauthorized': 'Email Invalido'}, status=status.HTTP_401_UNAUTHORIZED)
                        
    #         comparePasswords = check_password(password, user.password)            
                      
    #         #user4 = authenticate(username='admin', password='admin_admin')
    #         user5 = authenticate(username=user.email, password=password)

    #         print(user.username, 'aaa', user5)
    #         if comparePasswords:               

    #             refresh = RefreshToken.for_user(user5)    

    #             access_token = str(refresh.access_token)

    #             # Extrair valores relevantes do RefreshToken
    #             refresh_expires = refresh.access_token['exp']                
    #             #refresh_expires_readable = datetime.utcfromtimestamp(refresh_expires).strftime('%Y-%m-%d %H:%M:%S UTC')

    #             userCovertedDicionary = model_to_dict(user)

    #             response_data = {
    #             'message': 'Login bem-sucedido',   
    #             'user': userCovertedDicionary,             
    #             'token': access_token,
    #             'refreshToken': str(refresh),
    #             #'refresh_expires': refresh_expires_readable,
    #             }

    #             return Response(response_data, status=status.HTTP_200_OK)                
    #         else:
    #             return Response({'Unauthorized': 'Senha Invalida'}, status=status.HTTP_401_UNAUTHORIZED)


    # def authLogin(request,email, password):
    #     if email:        

    #         secret_key = 'sua_chave_secreta'            

    #         try:                
    #             user = User.objects.get(email=email)                         
    #         except:
    #             return Response({'Unauthorized': 'Email Invalido'}, status=status.HTTP_401_UNAUTHORIZED)
                        
    #         comparePasswords = check_password(password, user.password)            
           
    #         if comparePasswords:               

    #             payload = {
    #                 'email': user.email,
    #                 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)  # Tempo de expiração do token
    #             }
                
    #             token = jwt.encode(payload, secret_key, algorithm='HS256')

    #             return Response(token, status=status.HTTP_200_OK)                
    #         else:
    #             return Response({'Unauthorized': 'Senha Invalida'}, status=status.HTTP_401_UNAUTHORIZED)
