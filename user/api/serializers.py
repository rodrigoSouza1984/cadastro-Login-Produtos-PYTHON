from rest_framework.serializers import ModelSerializer, ValidationError
from user.models import User
from django.contrib.auth.hashers import make_password

from django.core.serializers import serialize
import json

from django.http import Http404
from django.forms.models import model_to_dict

from django.shortcuts import get_object_or_404

from rest_framework.response import Response

class UserSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = (  
            'id',
            'username',          
            'name', 
            'email', 
            'password', 
            'age', 
            'ownerApp', 
            'height', 
            'weight'   
        )

    def create(self, body):
        print(body)
    # Lógica personalizada de criação aqui
        # Verificar se 'name' está presente em validated_data
                
        if 'name' not in body:
            raise ValidationError("Name is required")
            
        if 'email' not in body:
            raise ValidationError("email is required")
        
        if '@' not in body['email']:
            raise ValidationError("Email Invalid'")

        if 'password' not in body:
            raise ValidationError("password is required")
        
        # Antes de criar o usuário, criptografe a senha
        body['password'] = make_password(body['password'])

        #body['password'] = bcrypt.hashpw(body['password'].encode("utf-8"), bcrypt.gensalt())
        user = User.objects.create(**body)
        return user


    def getUsers(self, request):

        # Configurações padrão
        default_page = 1
        default_take = 10

        # Obtém os parâmetros da consulta
        page = request.GET.get('page', default_page)
        take = request.GET.get('take', default_take)

        # Converte para inteiros
        try:
            page = int(page)
            take = int(take)
        except ValueError:
            return Response({"detail": "Os parâmetros 'page' e 'take' devem ser números inteiros."}, status=400)

        # Garante que os valores sejam positivos
        page = max(1, page)
        take = max(1, take)

        # Calcula o índice inicial e final para fatiar os resultados
        start_index = (page - 1) * take
        end_index = start_index + take

        users = User.objects.all()[start_index:end_index]           
        # usersInJson = serialize('json', users)        
        # usersJsonConverteds = json.loads(usersInJson)
        return json.loads(serialize('json', users))



    def getUserById(self, userId):
        try:
            user = User.objects.get(id=userId)            

            # Converte o objeto do modelo para um dicionário
            userCovertedDicionary = model_to_dict(user)

            return userCovertedDicionary
        except User.DoesNotExist:
            raise Http404("User does not exist")
        
    def getUserByEmail(self, email):
        try:            
            print('aaaa')
            user = User.objects.get(email=email)

            # Converte o objeto do modelo para um dicionário
            userCovertedDicionary = model_to_dict(user)

            return userCovertedDicionary
        except User.DoesNotExist:            
            raise Http404("User does not exist")
        

    def updatePatchUserById(self, body, userId):
        user = get_object_or_404(User, id=userId)
        userUpdated = UserSerializer(user, data=body, partial=True)
        
        if userUpdated.is_valid():
            userUpdated.save()
            return userUpdated.data
        else:
            return userUpdated.errors
        
    
    def updatePutUserById(self, body, userId):
        user = get_object_or_404(User, id=userId)
        userUpdated = UserSerializer(user, data=body)
        
        if userUpdated.is_valid():
            userUpdated.save()
            return userUpdated.data
        else:
            return userUpdated.errors
        

    
    def deleteUserByIds(self, userIds, userId):
        user = get_object_or_404(User, id=userId)

        users = User.objects.filter(id__in=userIds)
        
        users.delete()

        return True