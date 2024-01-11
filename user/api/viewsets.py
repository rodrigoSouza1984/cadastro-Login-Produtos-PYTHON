from rest_framework.viewsets import ModelViewSet
from user.models import User
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class UserViewSet2(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # @permission_classes([IsAuthenticated])
    permission_classes = (IsAuthenticated)


@api_view(['POST'])
def createUser(request):
    if request.method == 'POST':
        print(1, request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(2, serializer)
            userInstance = serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def getUsers(request):
    if request.method == 'GET':
        # Criar um objeto serializer
        serializer = UserSerializer()

        # Chamar o método getUsers do serializer
        users = serializer.getUsers(request)

        # Retornar na resposta da API
        return Response(users, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def getUserById(request, userId):
    if request.method == 'GET':   
           
        # Criar um objeto serializer        
        serializer = UserSerializer()
        # Chamar o método getUsers do serializer
        user = serializer.getUserById(userId)
        # Retornar na resposta da API
        return Response(user, status=status.HTTP_200_OK)
    
# @api_view(['GET'])
# def getUserByEmail(request, email):
#     if request.method == 'GET': 
#         print(12345)        
#         # Criar um objeto serializer        
#         serializer = UserSerializer()
#         # Chamar o método getUsers do serializer
#         try:
#             user = 1
#             #user = serializer.getUserByEmail(email)
#         except:
#            return Response({'aaaaa'}) 
#         # Retornar na resposta da API
#         return Response(user, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserByEmail(request, email):    
        print (request.headers['Authorization'], request.user.is_authenticated)
        return Response('aaaa', status=status.HTTP_200_OK)
    

@api_view(['PATCH'])
def updatePatchUserById(request, userId):
    if request.method == 'PATCH':

        serializer = UserSerializer()
        user = serializer.updatePatchUserById(request.data, userId) 

    if isinstance(user, dict):  # Verifica se user_data é um dicionário
        return Response(user, status=status.HTTP_200_OK)
    else:
        return Response(user, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def updatePutUserById(request, userId):
    if request.method == 'PUT':

        serializer = UserSerializer()
        user = serializer.updatePutUserById(request.data, userId) 

    if isinstance(user, dict):  # Verifica se user_data é um dicionário
        return Response(user, status=status.HTTP_200_OK)
    else:
        return Response(user, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def deleteUsersByIds(request, userId):
    if request.method == 'DELETE':
        serializer = UserSerializer()
        userIds = request.data
        
        if not userIds:
            return Response({"detail": "Nenhum ID de usuário fornecido para exclusão."}, status=status.HTTP_400_BAD_REQUEST)
                
        serializer.deleteUserByIds(userIds, userId)

        return Response(status=status.HTTP_204_NO_CONTENT)