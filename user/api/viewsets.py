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
        serializer = UserSerializer()
        users = serializer.getUsers(request)
        return Response(users, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def getUserById(request, userId):
    if request.method == 'GET':   
        serializer = UserSerializer()
        user = serializer.getUserById(userId)
        return Response(user, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserByEmail(request, email):
    if request.method == 'GET': 
        serializer = UserSerializer()
        
        try:
            user = 1
        except:
           return Response({'aaaaa'}) 
        return Response(user, status=status.HTTP_200_OK)
        

@api_view(['PATCH'])
def updatePatchUserById(request, userId):
    if request.method == 'PATCH':

        serializer = UserSerializer()
        user = serializer.updatePatchUserById(request.data, userId) 

    if isinstance(user, dict):  
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